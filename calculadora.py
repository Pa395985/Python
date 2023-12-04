print("****************************************")
print("Bem vindo a calculadora quântica do aluno")
print("****************************************")

numero_1= float(input("Digite o primeiro número:"))
numero_2= float(input("Digite o segundo número"))
while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")

    opcao = int(input())

    if opcao == 5:
        break

    elif opcao == 1:
        print(f"A soma de {numero_1} com o {numero_2} é :", numero_1 + numero_2)
    
    elif opcao == 2:
        print(f"A subtração de {numero_1} com o {numero_2} é :", numero_1 - numero_2)

    elif opcao == 3:
        print(f"A multiplicação de {numero_1} com o {numero_2} é :", numero_1 * numero_2)


    elif opcao == 4:
        print(f"A Divisão de {numero_1} com o {numero_2} é :", numero_1 / numero_2)
