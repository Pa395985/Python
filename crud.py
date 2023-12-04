# CRUD
#Importando Banco de dados

import mysql.connector 
# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'senai',
    database = 'loja_ii'
    )

cursor = conexao.cursor()

# Criar uma tabela cliente_vip

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente_vip(
        idcliente INT  AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        telefone INT(13),
        email VARCHAR(45) NOT NULL,
        dpf INT(255) NOT NULL
        )'''
)


    

# funcao para inserir dados na tabela cliente_vip

def inserir_cliente(nome, endereco, telefone, email, dpf):
    query = 'INSERT INTO cliente_vip (nome, endereco, telefone, email, dpf) VALUES = (%s, %s, %s, %s, %s)'
    values = (nome, endereco, telefone, email, dpf)
    cursor.execute(query, values)
    conexao.commit()

# Funão para listar todos os clientes

def listar_cliente():
    cursor.execute('SELECT * FROM cliente-vip')
    cliente = cursor.fetchall()
    for clientes in cliente:
        print(clientes)

#Funçao par atualizar a tabela cliente_vip

def atualizar_cliente_vip(idcliente, nome, endereco, telefone, email, dpf):
    query = 'UPDATE cliente_vip SET nome = %s, endereco = %s, telefone = %s, email = %s, email = %s, dpf = %s WHERE id cliente = %s'
    values = (idcliente, nome, endereco, telefone, email, dpf)
    cursor.execute(query, values)


# Funçaõ pra deletar um cliente

def delete_cliente(idcliente):
    query = 'DELETE FROM cliente_vip WHERE idcliente = %s'
    values = (idcliente,)
    cursor.execute(query, values)

# Exemplo de uso

inserir_cliente('Roberto', 'Rua do Senai', '9804520', 'elio@elio.com', '2324567')
#inserir_cliente('Guilherme','Rua do Infinito e além', '123456454', 'galvesmacedo@gmail', '123457')

#delete_cliente(1)


#pip install update
#