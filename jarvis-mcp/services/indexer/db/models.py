from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_PATH = '/data/mcp_index.db'
engine = create_engine(f'sqlite:///{DB_PATH}')
Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_db():
    return Session()

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    path = Column(String, unique=True)

class Chunk(Base):
    __tablename__ = 'chunks'
    id = Column(Integer, primary_key=True)
    path = Column(String)
    embedding = Column(LargeBinary)
    text = Column(String)

class Symbol(Base):
    __tablename__ = 'symbols'
    id = Column(Integer, primary_key=True)
    path = Column(String)
    symbols = Column(String)
