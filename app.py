import tkinter as tk
from tkinter import messagebox
from entry import Inserir_dados, exibir_grafico

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("300x300")

# 1º - Widgets de entrada
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


# 2º - Função que só coleta os campos e chama a lógica do entry.py
def ao_clicar_inserir():
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

    Inserir_dados(nome, email, salario, cargo)

    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_salario.delete(0, tk.END)
    entrada_cargo.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")


# 3º - Botões
tk.Button(janela, text="Inserir", command=ao_clicar_inserir).pack(pady=10)
tk.Button(janela, text="Ver Gráfico", command=exibir_grafico).pack()

janela.mainloop()