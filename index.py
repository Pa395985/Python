import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira interface com Tkinter")

#Criando um label ( rótulo)
rotulo = tk.Label(janela, text="Nome")

#Adicionando o rótulo a janela
rotulo.pack()

#Criando um botão ( button)
def mensagem():
    print("Você clicou")

btn_clicar= tk.Button(janela, text="Clique em mim", command= mensagem())
btn_clicar.pack()
                       


#Entry ( Entrda de Texto)
entrada = tk.Entry(janela)
entrada.pack()

#Field/Text (Área de Texto)
area_de_texto = tk.Text(janela)
area_de_texto.pack()

#Frame (Quadro)
frame = tk.Frame(janela)
frame.pack

#Checkbutton ( Botão de seleção)
check = tk.Checkbutton(janela, text="Opção 1" )
check2 = tk.Checkbutton(janela, text="Opção 2")
check.pack()
check2.pack()

#Radiobutton (Botão de seleção redondo)

radio1= tk.Radiobutton(janela, text="Opção 1", value=3)
radio2= tk.Radiobutton(janela, text="Opção 2", value=4)
radio1.pack()
radio2.pack()

#Adicionando um lista ( Caixa de Listagem)
lista = tk.Listbox(janela)
lista.insert(1,"São Paulo")
lista.insert(2,"Bauru")
lista.insert(3,"Ribeirão Preto")
lista.pack()

#chamando o método de execução
janela.mainloop()