import mysql Connector

# Configurações da conexão com o banco de dados

config = {
    'user": se_usuário,'
    'pasword': 'sua_senha',
    'host': 'localhost',
    'database': 'nome_do_banco_de_dados'}

# Estabelecer a conexão com o banco de dados

Conexão = mysql.connector
connect(**config)


# Criar um cursor para executar consultas SQL 
cursor = conexão.cursor()

# Exemplo de consulta SQL
SelecionarDB = "Use loja_ii;"

consulta = "INSERT INTO clientes("nome", "endereço", "telefone", "e-mail", "cpf") VALUES

# Dados novo cliente 
nova_cliente = ("Ana Paula", "Rua do Bosque",123456, "ana@ana", 321654987)


# Executar a consulta 
cursor.execute(SelecionarDB)
cursor.execute(consulta)

# Recuperar os resultados 
Resultados = cursor Fetchall()

# Imprimir os resultados
for linha in Resultados:
    print(linha,"\n")

# Fechar o cursor e a conexão
Cursor.close
Conexão.close()





