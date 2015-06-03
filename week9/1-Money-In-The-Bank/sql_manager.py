import sqlite3
from Client import Client
from Init import create_clients_table
import time
import hashlib


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def get_email(username):
    email_query = "SELECT email from clients WHERE username = ?"
    cursor.execute(email_query, (username,))
    email = cursor.fetchone()
    if type(email) is tuple:
        return email[0]



    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    password = hashit(password)
    insert_sql = "INSERT INTO clients (username, password, email) VALUES (?, ?, ?)"
    cursor.execute(insert_sql, (username, password, email))
    conn.commit()


def login(username, password):
    password = hashit(password)
    check_query = "SELECT login_attempts, last_attempt FROM clients WHERE username = ?"
    cursor.execute(check_query, (username,))
    last_attempt = cursor.fetchone()
    if type(last_attempt) is not tuple:
        return -2
    if last_attempt[0] % 5 == 0 and last_attempt[0] > 0 and time.time() - last_attempt[1] < 300:
        return -1

    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        reset_attempts_query = "UPDATE clients SET login_attempts = 0 WHERE username = ?"
        cursor.execute(reset_attempts_query, (username,))
        conn.commit()
        return Client(user[0], user[1], user[2], user[3])

    else:
        timenow = time.time()
        update_query = "UPDATE clients SET login_attempts = login_attempts+1, last_attempt = ? WHERE username = ?"
        cursor.execute(update_query, (timenow, username))
        conn.commit()
        return 0


def hashit(password):
    byte_password = str.encode(password)
    hash_object = hashlib.sha1(byte_password)
    return(hash_object.hexdigest())
