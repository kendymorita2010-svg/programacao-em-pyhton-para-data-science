import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3

# ---- Banco de dados ----
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

# ---- Inserção inicial dos alunos ----
cursor.execute('SELECT COUNT(*) FROM clientes')
if cursor.fetchone()[0] == 0:
    cursor.execute('INSERT INTO clientes (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Ana', 'ana@gmail.com', 4500.0, 'Analista'))
    cursor.execute('INSERT INTO clientes (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Kaio', 'kaka@gmail.com', 3500.0, 'Estagiário'))
    cursor.execute('INSERT INTO clientes (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Felipe', 'fe@gmail.com', 1500.0, 'Menor Ap.'))
    cursor.execute('INSERT INTO clientes (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Bernardo', 'ber@gmail.com', 9500.0, 'Coordenador'))
    banco.commit()

# ---- Interface ----
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("300x300")

tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Email").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

tk.Label(janela, text="Salário").pack()
entrada_salario = tk.Entry(janela)
entrada_salario.pack()

tk.Label(janela, text="Cargo").pack()
entrada_cargo = tk.Entry(janela)
entrada_cargo.pack()


# ---- Funções ----
def Inserir_dados():
    nome = entrada_nome.get()
    email = entrada_email.get()
    salario = entrada_salario.get()
    cargo = entrada_cargo.get()

    if not nome or not email or not salario or not cargo:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    try:
        salario = float(salario)
    except ValueError:
        messagebox.showerror("Erro", "Salário inválido.")
        return

    cursor.execute(
        'INSERT INTO clientes (nome, email, salario, cargo) VALUES (?, ?, ?, ?)',
        (nome, email, salario, cargo)
    )
    banco.commit()

    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_salario.delete(0, tk.END)
    entrada_cargo.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")


def exibir_grafico():
    cursor.execute('SELECT nome, salario FROM clientes')
    dados = cursor.fetchall()

    if not dados:
        messagebox.showwarning("Aviso", "Nenhum dado para exibir.")
        return

    nomes = [linha[0] for linha in dados]
    salarios = [linha[1] for linha in dados]

    plt.bar(nomes, salarios)
    plt.xlabel('Nome')
    plt.ylabel('Salário')
    plt.title('Salário por Cliente')
    plt.show()


# ---- Botões ----
tk.Button(janela, text="Inserir", command=Inserir_dados).pack(pady=10)
tk.Button(janela, text="Ver Gráfico", command=exibir_grafico).pack()

janela.mainloop()