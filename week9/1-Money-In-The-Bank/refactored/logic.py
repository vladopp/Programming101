from Init import Client, engine
from sqlalchemy.orm import Session
import hashlib
import time

session = Session(bind=engine)


def hashit(password):
    byte_password = str.encode(password)
    hash_object = hashlib.sha1(byte_password)
    return(hash_object.hexdigest())


def register(username, password, email):
    password = hashit(password)
    session.add(Client(username=username, password=password, email=email))
    session.commit()


def login(username, password):
    password = hashit(password)
    try:
        user = session.query(Client).filter(Client.username == username).filter(Client.password == password).one()
    except Exception:
        pass
    print(user.username)
    return user


def change_pass(password, logged_user):
    password = hashit(password)
    logged_user.password = password
    session.commit()


def change_message(new_message, logged_user):
    logged_user.message = new_message
    session.commit()
