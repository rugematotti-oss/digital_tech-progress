import os
import sys
import streamlit as st

# Permet d'importer src/ et bonus/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.card import build_card
from bonus.wordcloud.wordcloud_generator import generate_wordcloud
from bonus.author.author_books import find_books_by_author, download_books


st.set_page_config(
    page_title="Bookworm Frontend",
    layout="wide"
)


def safe_build_card(book_id: int):
    try:
        return build_card(book_id)
    except Exception as e:
        return {"error": str(e)}


def display_info(info: dict):
    st.subheader("Informations du livre")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**ID :** {info.get('id', 'Unknown')}")
        st.write(f"**Titre :** {info.get('title', 'Unknown')}")
    with col2:
        st.write(f"**Auteur(s) :** {info.get('authors', 'Unknown')}")
        st.write(f"**Bookshelves :** {info.get('bookshelves', 'Unknown')}")


def display_lexdiv(lexdiv: dict):
    st.subheader("Diversité lexicale")

    col1, col2, col3 = st.columns(3)
    col1.metric("TOK", lexdiv.get("tok", 0))
    col2.metric("TYP", lexdiv.get("typ", 0))
    col3.metric("HAP", lexdiv.get("hap", 0))

    col4, col5, col6 = st.columns(3)
    col4.metric("TTR", lexdiv.get("ttr", 0.0))
    col5.metric("MWL", lexdiv.get("mwl", 0.0))
    col6.metric("MWF", lexdiv.get("mwf", 0.0))


def display_topics(topics: dict):
    st.subheader("Topics par section")

    for section, words in topics.items():
        st.markdown(f"**Section {section}**")
        if words:
            st.write(", ".join(words))
        else:
            st.write("Aucun topic trouvé.")


def display_entities(entities: dict):
    st.subheader("Entités")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Personnages**")
        if entities.get("characters"):
            for character in entities["characters"]:
                st.write(f"- {character}")
        else:
            st.write("Aucun personnage trouvé.")

    with col2:
        st.markdown("**Lieux**")
        if entities.get("locations"):
            for location in entities["locations"]:
                st.write(f"- {location}")
        else:
            st.write("Aucun lieu trouvé.")


def display_summary(summary: str):
    st.subheader("Résumé")
    st.write(summary if summary else "Aucun résumé disponible.")


def display_similar(similar: list):
    st.subheader("Livres similaires")
    if similar:
        for title in similar:
            st.write(f"- {title}")
    else:
        st.write("Aucun livre similaire trouvé.")


def display_wordcloud(book_id: int):
    st.subheader("Word Cloud")

    try:
        image_path = generate_wordcloud(book_id)
        st.image(image_path, caption=f"Word Cloud - Book {book_id}", use_container_width=True)
    except Exception as e:
        st.error(f"Impossible de générer la word cloud : {e}")


def author_section():
    st.header(" Recherche par auteur")

    if "author_books" not in st.session_state:
        st.session_state.author_books = None
    if "author_name" not in st.session_state:
        st.session_state.author_name = ""
    if "download_results" not in st.session_state:
        st.session_state.download_results = None

    with st.form("author_search_form"):
        author_name = st.text_input(
            "Nom de l'auteur",
            value=st.session_state.author_name,
            placeholder="Ex: Carroll, Lewis"
        )
        submitted = st.form_submit_button("Rechercher")

    if submitted:
        if not author_name.strip():
            st.warning("Veuillez entrer un nom d'auteur.")
        else:
            books = find_books_by_author(author_name)
            st.session_state.author_name = author_name
            st.session_state.author_books = books
            st.session_state.download_results = None

    if st.session_state.author_books is not None:
        books = st.session_state.author_books

        if not books:
            st.error("Aucun livre trouvé.")
        else:
            st.success(f"{len(books)} livre(s) trouvé(s) pour : {st.session_state.author_name}")

            for book in books[:20]:
                st.write(f" {book['title']} (ID: {book['id']})")

            if st.button("Télécharger les livres de cet auteur"):
                with st.spinner("Téléchargement en cours..."):
                    results = download_books(books[:10])
                    st.session_state.download_results = results

    if st.session_state.download_results is not None:
        st.subheader("Résultats du téléchargement")
        for result in st.session_state.download_results:
            st.write(f"{result['title']} → {result['status']}")


def main():
    st.title(" Bookworm")
    st.write("Frontend interactif pour explorer les analyses NLP des livres Gutenberg.")

    tab1, tab2 = st.tabs([" Analyse par ID", " Recherche par auteur"])

    with tab1:
        if "card_result" not in st.session_state:
            st.session_state.card_result = None
        if "last_book_id" not in st.session_state:
            st.session_state.last_book_id = 11

        book_id = st.number_input(
            "Entrez un Book ID Gutenberg",
            min_value=1,
            step=1,
            value=int(st.session_state.last_book_id)
        )

        if st.button("Analyser le livre"):
            with st.spinner("Analyse en cours..."):
                st.session_state.last_book_id = book_id
                st.session_state.card_result = safe_build_card(book_id)

        if st.session_state.card_result is not None:
            result = st.session_state.card_result

            if "error" in result:
                st.error(f"Erreur : {result['error']}")
            else:
                display_info(result.get("info", {}))

                st.divider()
                display_lexdiv(result.get("lexdiv", {}))

                st.divider()
                display_topics(result.get("topics", {}))

                st.divider()
                display_entities(result.get("entities", {}))

                st.divider()
                display_summary(result.get("summary", ""))

                st.divider()
                display_similar(result.get("similar", []))

                st.divider()
                display_wordcloud(st.session_state.last_book_id)

    with tab2:
        author_section()


if __name__ == "__main__":
    main()