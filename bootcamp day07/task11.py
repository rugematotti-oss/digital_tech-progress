from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
class Country(Base):
    __tablename__ = 'countries'
    
    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    laureates_born = relationship('Laureate', foreign_keys='Laureate.born_country_id', back_populates='born_country')
    laureates_died = relationship('Laureate', foreign_keys='Laureate.died_country_id', back_populates='died_country')
    prizes = relationship('Prize', back_populates='affiliation_country')


class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    prizes = relationship('Prize', back_populates='category')


class Laureate(Base):
    __tablename__ = 'laureates'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String)
    born = Column(String)
    died = Column(String)
    born_country_id = Column(String, ForeignKey('countries.code'))
    died_country_id = Column(String, ForeignKey('countries.code'))

    born_country = relationship('Country', foreign_keys=[born_country_id], back_populates='laureates_born')
    died_country = relationship('Country', foreign_keys=[died_country_id], back_populates='laureates_died')
    prizes = relationship('Prize', back_populates='laureate')


class Prize(Base):
    __tablename__ = 'prizes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    laureate_id = Column(Integer, ForeignKey('laureates.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    year = Column(Integer, nullable=False)
    affiliation_country_id = Column(String, ForeignKey('countries.code'))
    
    laureate = relationship('Laureate', back_populates='prizes')
    category = relationship('Category', back_populates='prizes')
    affiliation_country = relationship('Country', back_populates='prizes')


def init_sqla(db_name: str):
    engine = create_engine(f'sqlite:///{db_name}')
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    return session