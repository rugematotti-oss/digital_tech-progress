def read_chat_messages(token: str, chat_id: str) -> dict:
    url = f"https://graph.microsoft.com/v1.0/chats/{chat_id}/messages"
    headers