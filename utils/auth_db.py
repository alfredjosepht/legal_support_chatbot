import sqlite3
import hashlib
import os

DB_PATH = "data/users.db"


def get_db():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def register_user(username: str, password: str) -> bool:
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password(password))
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False


def authenticate_user(username: str, password: str) -> bool:
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return False

    return row[0] == hash_password(password)
