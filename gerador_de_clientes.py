# importações
import random
import datetime
import uuid
import hashlib
import mysql.connector


# funções
def gera_ID():

    id = uuid.uuid4()

    id_sha256 = hashlib.sha256()
    id_sha256.update(id.bytes)

    id_str = id_sha256.hexdigest()
    return id_str

def gera_cpf():

    cpf = uuid.uuid4()

    cpf_sha256 = hashlib.sha256()
    cpf_sha256.update(cpf.bytes)

    cpf_str = cpf_sha256.hexdigest()
    return cpf_str

def gera_nome_completo():

    indice_random_nome = random.randrange(0, 97)
    indice_random_sobrenome = random.randrange(0, 98)
    nome = nomes[indice_random_nome] + " " + sobrenomes[indice_random_sobrenome]
    return nome

def gera_conta():

    conta = uuid.uuid4()

    conta_sha256 = hashlib.sha256()
    conta_sha256.update(conta.bytes)

    conta_str = conta_sha256.hexdigest()
    return conta_str
    
def gera_n_cartao():

    n_cartao_gerado = uuid.uuid4()

    n_cartao_gerado_sha256 = hashlib.sha256()
    n_cartao_gerado_sha256.update(n_cartao_gerado.bytes)

    n_cartao_gerado_str = n_cartao_gerado_sha256.hexdigest()
    return n_cartao_gerado_str

def gera_saldo():

    saldo_gerado = round(random.uniform(111.11, 9999.99), 2)
    return saldo_gerado


def gera_senha():

    senha_gerada = uuid.uuid4()

    senha_gerada_sha256 = hashlib.sha256()
    senha_gerada_sha256.update(senha_gerada.bytes)

    senha_gerada_str = senha_gerada_sha256.hexdigest()
    return senha_gerada_str

def gera_data_nascimento():

    data = datetime.date(random.randint(1960, 1998), random.randint(1, 12), random.randint(1, 12))
    return data


# código
nomes = ["Helena", "Miguel", "Alice", "Arthur", "Laura", "Heitor", "Manuela", "Valentina", "Davi", "Sophia", "Theo", "Isabela", "Lorenzo", "Heloisa", "Gabriel", "Luiza", "Pedro", "Julia", "Benjamin", "Lorena", "Matheus", "Livia", "Lucas", "Maria Luiza", "Nicolas", "Cecília", "Joaquim", "Eloa", "Samuel", "Giovanna", "Henrique", "Maria Clara", "Rafael", "Maria Eduarda", "Guilherme", "Mariana", "Enzo", "Lara", "Murilo", "Beatriz", "Benicio", "Antonela", "Gustavo", "Maria Julia", "Isaac", "Emanuelly", "João Miguel", "Isadora", "Lucca", "Ana Clara", "Enzo Gabriel", "Melissa", "Pedro Henrique", "Ana Luiza", "João Pedro", "Esther", "Pietro", "Lavinia", "Anthony", "Maite", "Daniel", "Maria Cecilia", "Bryan", "Maria Alice", "Davi Lucca", "Sarah", "Leonardo", "Elisa", "Vicente", "Liz", "Eduardo", "Yasmin", "Gael", "Isabelly", "Antonio", "Alicia", "Vitor", "Clara", "Noah", "Isis", "Caio", "Rebecca", "João", "Rafaela", "Emanuel", "Marina", "Caua", "Ana Laura", "João Lucas", "Maria Helena", "Calebe", "Agatha", "Enrico", "Gabriela", "Vinicius", "Catarina", "Bento"]
sobrenomes = ["da Silva", "dos Santos", "Pereira", "Alves", "Ferreira", "de Oliveira", "Silva", "Rodrigues", "de Souza", "Gomes", "Santos", "Oliveira", "Ribeiro", "Martins", "Golçalves", "Soares", "Barbosa", "Lopes", "Vieira", "Souza", "Fernandes", "Lima", "Costa", "Bastista", "Dias", "Moreira", "de Lima", "de Sousa", "Nunes", "da Costa", "de Almeida", "Mendes", "Carvalho", "Araujo", "Cardoso", "Teixeira", "Marques", "do Nascimento", "Almeida", "Ramos", "Machado", "Rocha", "Nascimento", "de Araujo", "da Conceiçao", "Bezerra", "Sousa", "Borges", "Santana", "de Carvalho", "Aparecido", "Pinto", "Pinheiro", "Monteiro", "Andrade", "Leite", "Correa", "Nogueira", "Garcia", "de Freitas", "Henrique", "Tavares", "Coelho", "Pires", "de Paula", "Correia", "Miranda", "de Jesus", "Duarte", "Freitas", "Barros", "de Andrade", "Campos", "Santos", "de Melo", "da Cruz", "Reis", "Guimaraes", "Moraes", "do Carmo", "dos Reis", "Viana", "de Castro", "Silveira", "Moura", "Brito", "Neves", "Carneiro", "Melo", "Medeiros", "Cordeiro", "Conceiçao", "Farias", "Dantas", "Cavalcante", "da Rocha", "de Assis", "Braga", "Cruz", "Siqueira"]

for i in range(20000):
    id_gerada = gera_ID()
    cpf_gerado = gera_cpf()
    nome_gerado = gera_nome_completo()
    conta_gerada = gera_conta()
    cartao_gerado = gera_n_cartao()
    saldo_gerado = gera_saldo()
    senha_gerada = gera_senha()
    data_de_nascimento_gerada = gera_data_nascimento()

    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DEcimasenha@883!",
    database="sistema_transacional"
    )

    cursor = conexao.cursor()

    sql = ("INSERT INTO tab_clientes "
        "(ID, CPF, NOME, CONTA, CARTAO, SALDO, SENHA, DATA_DE_NASCIMENTO) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data_sql = (id_gerada, cpf_gerado, nome_gerado, conta_gerada, cartao_gerado, saldo_gerado, senha_gerada, data_de_nascimento_gerada)

    cursor.execute(sql, data_sql)

    conexao.commit()
