import tkinter as tk


janela = tk.Tk()
largura = "500"
altura= "500"
janela.geometry(f"{largura}x{altura}")
janela.title("Calculadora Geométrica")

#Entrada de números
entrada1 = float(tk.Entry(janela))
entrada2 = float(tk.Entry(janela))

#Botão que efetua uma oparacao
def efetua_soma():
    valor1 = (entrada1.get())
    valor2 = (entrada2.get())
    resultado = valor1 + valor2
    lbl_resultado.config(text=f"Resultado: {resultado}")

def efetua_subtracao():
    valor1 = (entrada1.get())
    valor2 = (entrada2.get())
    resultado = valor1 - valor2
    lbl_resultado.config(text=f"Resultado: {resultado}")

def efetua_multiplicacao():
    valor1 = (entrada1.get())
    valor2 = (entrada2.get())
    resultado = valor1 * valor2
    lbl_resultado.config(text=f"Resultado: {resultado}")


def efetua_divisao():
    try:  
    
        valor1 = (entrada1.get())
        valor2 = (entrada2.get())

    except:

        if( valor2 != 0 ):
            resultado = valor1 / valor2
            lbl_resultado.config(text=f"Resultado: {resultado}")
    else:
        print("Erro, divisão por zero")



#Local onde é exibido o resultado
lbl_resultado= tk.Label(janela, text="Exibe resultado")

botao_calcular= tk.Button(janela,text="Calcular", command=efetua_soma())

entrada1.pack()
entrada2.pack()
botao_calcular.pack()
lbl_resultado.pack()

janela.mainloop()

