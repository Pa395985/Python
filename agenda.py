import tkinter as tk
from tkinter import messagebox
import mysql.connector

class AplicacaoTkinter:
    def __init__(self, janela, conexao):
        self.janela = janela
        self.conexao = conexao

        self.janela.title("Agenda de Amigos")

        self.label_nome = tk.Label(janela, text="Nome")
        self.label_email = tk.Label(janela, text="Email")
        self.label_telefone = tk.Label(janela, text="Telefone")

        self.entry_nome = tk.Entry(janela)
        self.entry_email = tk.Entry(janela)
        self.entry_telefone = tk.Entry(janela)

        self.botao_inserir = tk.Button(janela, text="Inserir", command=self.inserir_dados)
        self.botao_atualizar = tk.Button(janela, text="Atualizar", command=self.atualizar_dados)
        self.botao_listar = tk.Button(janela, text="Listar", command=self.listar_dados)
        self.botao_deletar = tk.Button(janela, text="Deletar", command=self.deletar_dados)

        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.label_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.label_telefone.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.entry_nome.grid(row=0, column=1, columnspan=2, pady=10, sticky="ew")
        self.entry_email.grid(row=1, column=1, columnspan=2, pady=10, sticky="ew")
        self.entry_telefone.grid(row=2, column=1, columnspan=2, pady=10, sticky="ew")

        self.botao_inserir.grid(row=3, column=0, columnspan=2, pady=10)
        self.botao_atualizar.grid(row=3, column=2, columnspan=2, pady=10)
        self.botao_listar.grid(row=3, column=4, columnspan=2, pady=10)
        self.botao_deletar.grid(row=3, column=6, columnspan=2, pady=10)

        self.janela.columnconfigure(1, weight=1)
        self.janela.rowconfigure(4, weight=1)

        self.janela.bind("<Configure>", self.atualizar_layout)

    def executar_query(self, query, parametros=None):
        cursor = self.conexao.cursor()
        try:
            if parametros:
                cursor.execute(query, parametros)
            else:
                cursor.execute(query)
            self.conexao.commit()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução da consulta: {str(e)}")
        finally:
            cursor.close()

    def inserir_dados(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()

        if nome and email and telefone:
            query = "INSERT INTO amigo (nome, email, telefone) VALUES (%s, %s, %s)"
            parametros = (nome, email, telefone)
            self.executar_query(query, parametros)
            messagebox.showinfo("Sucesso", "Dados inseridos com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def atualizar_dados(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()

        if nome and email and telefone:
            query = "UPDATE amigo SET email = %s, telefone = %s WHERE nome = %s"
            parametros = (email, telefone, nome)
            self.executar_query(query, parametros)
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def listar_dados(self):
        query = "SELECT * FROM amigo"
        cursor = self.conexao.cursor(dictionary=True)
        try:
            cursor.execute(query)
            resultados = cursor.fetchall()
            messagebox.showinfo("Listar Amigos", str(resultados))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar lista: {str(e)}")
        finally:
            cursor.close()

    def deletar_dados(self):
        nome = self.entry_nome.get()

        if nome:
            query = "DELETE FROM amigo WHERE nome = %s"
            parametros = (nome,)
            self.executar_query(query, parametros)
            messagebox.showinfo("Sucesso", "Dados excluídos com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Preencha o campo 'Nome'.")

    def atualizar_layout(self, event):
        
        pass

conexao = mysql.connector.connect(user="root", password="senai", host="localhost", database="agenda")

janela = tk.Tk()
app = AplicacaoTkinter(janela, conexao)
janela.mainloop()

conexao.close()
