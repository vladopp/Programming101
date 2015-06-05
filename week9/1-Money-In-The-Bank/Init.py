from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
import settings

Base = declarative_base()


class Client(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    balance = Column(Integer, default=0)
    message = Column(String)
    login_attempts = Column(Integer, default=0)
    last_attempt = Column(Integer, default=0)
    email = Column(String)

engine = create_engine(settings.DATABASE)


def create_db():
    Base.metadata.create_all(engine)
