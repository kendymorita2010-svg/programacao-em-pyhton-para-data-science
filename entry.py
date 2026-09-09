# entry.py
import sqlite3

banco = sqlite3.connect('dados.db')
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    salario REAL NOT NULL,
    cargo TEXT NOT NULL
)''')
banco.commit()