import mysql.connector

config = {
    'user' : 'root',
    'password' : 'senai',
    'host' : 'localhost',
    'database' : 'loja_ii'
}


# Estabecer a conexao com o banco de dados
conexao = mysql.connector.connect(**config)

# Criar um cursor para executar consulta SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
#selecionarDB = "use loja_ii;"
consulta = "SELECT * FROM clientes"

inserirCliente = """INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf) 
VALUES ("Ana", "Rua do Bosque", 123456789 "ana@ana.com", 236548945) (%s,%s,%i,%s,%i)"""

novo_cliente = ("Ana", "Rua do Bosque", 123456789, "ana@ana.com", 236548945)

# Executar a consulta
#cursor.execute(selecionarDB)
cursor.execute(consulta)
cursor.execute(inserirCliente, novo_cliente)

#Recuperar os resultados
resultados = cursor.fetchall()

# Imprimir os resultados
for linha in resultados:
    print(linha, "\n" )

# Fechar o cursor e a conexão
cursor.close()
conexao.close()