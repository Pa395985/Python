import mysql.connector

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host='localhost', 
    user= 'root', 
    password= 'senai',
    database= 'loja_ii'
)

cursor = conn.cursor()

# Script para criar uma tabela chamada cliente_vip
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente_especial (
               idcliente INT AUTO_INCREMENT PRIMARY KEY,
               nome VARCHAR(45) NOT NULL,
               endereco VARCHAR(255) NOT NULL,
               telefone INT(13),
               email VARCHAR(45) NOT NULL,
               cpf INT(20) NOT NULL
               )''')

#Função para inserir dados na tabela cliente

def inserir_cliente(nome, endereco, telefone, email, cpf):
    query = 'INSERT INTO cliente_especial (nome, endereco, telefone, email, cpf) VALUES (%s, %s, %s, %s, %s)'
    values = (nome, endereco, telefone,email, cpf)
    cursor.execute(query, values)
    conn.commit()

#Função para listar todos os clientes

def listar_cliente():
    cursor.execute('SELECT * FROM cliente_especial')
    cliente = cursor.fetchall()
    for clientes in cliente:
        print(clientes)

#Função para atualizar a tabela cliente_vip

def atualizar_cliente_vip(idcliente, nome, endereco, telefone, email, cpf):
    query= 'UPDATE cliente_especial SET nome = %s, endereco = %s, telefone = %s, email=%s, cpf=%s WHERE idcliente = %s'
    values = (nome, endereco, telefone, email, cpf, idcliente)
    cursor.execute(query, values)

#Função para deletar um cliente

def delete_cliente(idcliente):
    query= 'DELETE FROM cliente_especial WHERE idcliente = %s'
    values = (idcliente,)
    cursor.execute(query, values)

#Exemplo de uso:
inserir_cliente('Guilherme','Rua do Infinito e além', '123456454', 'galvesmacedo@gmail', '123457')

#delete_cliente(1)




