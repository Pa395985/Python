import tkinter as tk
from tkinter import PhotoImage
import os

def exibir_imagem():
    caminho_imagem = os.path.abspath(".\\Agenda\\img\\praia.jpg")
    
    try:
        imagem = PhotoImage(file=caminho_imagem)
        rotulo_imagem.config(image=imagem)
        rotulo_imagem.image = imagem
    except tk.TclError:
        print(f"Erro: Não foi possível abrir a imagem em {caminho_imagem}")

# Criando nossa janela
janela = tk.Tk()
janela.title("Inserindo Imagens")

# Criar um botão para carregar e exibir a imagem
botao_carregar_imagem = tk.Button(janela, text="Carregar Imagem", command=exibir_imagem)
botao_carregar_imagem.pack(pady=10)

# Criar um rótulo para exibir a imagem
rotulo_imagem = tk.Label(janela)
rotulo_imagem.pack(pady=10)

janela.mainloop()

