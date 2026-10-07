from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosApp.db"        #"mysql+pymysql://root:teju*2008@127.0.0.1:3306/TodoApplicationDatabase" "postgresql://postgres:teju1220@localhost/TodoApplicationDatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})

SessionLocal = sessionmaker(autoflush = False, autocommit = False, bind = engine)

Base = declarative_base()