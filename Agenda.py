"""agenda = [ {"Nome": "Ademir", "Telefone":111, "Email": "aaa@com", "Endereço": " Rua AAA" }, {"Nome": "Luciene", "Telefone":222, "Email": "bbb@com", "Endereço": " Rua BBB" },{"Nome": "Gabriel", "Telefone":333, "Email": "ccc@com", "Endereço": " Rua CCC" }, {"Nome": "Jean", "Telefone":444, "Email": "ddd@com", "Endereço": " Rua DDD" } ]

for i in agenda:
 print(i, "\n")"""


contatos = {}

while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone do contato: ")
        contatos[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso!")
    
       

    elif escolha == "2":
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in contatos:
            print(f"Nome: {nome}, Telefone: {contatos[nome]}")
        else:
            print("Contato não encontrado.")

    elif escolha == "3":
        break

    else:
        print("Opção inválida. Tente novamente.")







