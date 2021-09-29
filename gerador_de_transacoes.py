# importações
import mysql.connector
import random
import uuid
import hashlib


# funções
def gera_id_transacao():

    id_gerada = uuid.uuid4()

    id_sha256 = hashlib.sha256()
    id_sha256.update(id_gerada.bytes)

    id_str = id_sha256.hexdigest()
    return id_str

def sorteia_cliente():
    conexao = mysql.connector.connect(host="localhost", user="root", password="DEcimasenha@883!", database="sistema_transacional")
    cursor = conexao.cursor()

    query = ("SELECT * FROM tab_clientes ORDER BY RAND() LIMIT 1")

    cursor.execute(query)

    lista = []

    for (id, cpf, nome, conta, cartao, saldo, senha, data_de_nascimento) in cursor:

        lista_temp = [id, cpf, nome, conta, cartao, saldo, senha, data_de_nascimento]
        lista.append(lista_temp)

    cursor.close()

    conexao.close()

    return lista

def sorteia_estabelecimento():
    conexao = mysql.connector.connect(host="localhost", user="root", password="DEcimasenha@883!", database="sistema_transacional")
    cursor = conexao.cursor()

    query = ("SELECT * FROM tab_estabelecimentos ORDER BY RAND() LIMIT 1")

    cursor.execute(query)

    lista = []

    for (id, nome, endereco, cidade, tipo) in cursor:

        lista_temp = [id, nome, endereco, cidade, tipo]
        lista.append(lista_temp)

    cursor.close()

    conexao.close()

    return lista

def gera_valor_transacao():
    valor = round(random.uniform(11.11, 299.99), 2)

    return valor

def gera_data_transacao():

    ano = "2020"
    mes = "01"
    dia_str = str(random.randrange(1,32))
    dia_fill = dia_str.zfill(2)

    data_gerada = ano + mes + dia_fill

    return data_gerada


def gera_hora_transacao():

    numero_aleatorio = random.randrange(1, 100)

    if (numero_aleatorio >= 40):

        n_aleatorio_pico = random.randrange(0,5)

        hora_pico = ["12", "13", "14", "18", "19"]

        hora = hora_pico[n_aleatorio_pico] 
        minuto_str = str(random.randrange(1,60))
        minuto_fill = minuto_str.zfill(2)
        segundo_str = str(random.randrange(1,60))
        segundo_fill = segundo_str.zfill(2)

        hora_gerada = hora + minuto_fill + segundo_fill
    
    elif (numero_aleatorio >= 10 and numero_aleatorio <= 40):

        n_aleatorio_normal = random.randrange(0,9)

        hora_normal = ["08", "09", "10", "11", "15", "16", "17", "20", "21"]

        hora = hora_normal[n_aleatorio_normal]
        minuto_str = str(random.randrange(1,60))
        minuto_fill = minuto_str.zfill(2)
        segundo_str = str(random.randrange(1,60))
        segundo_fill = segundo_str.zfill(2)

        hora_gerada = hora + minuto_fill + segundo_fill

    elif (numero_aleatorio < 10):

        n_aleatorio_vale = random.randrange(0,10)

        hora_vale = ["00", "01", "02", "03", "04", "05", "06", "07", "22", "23"]

        hora = hora_vale[n_aleatorio_vale]
        minuto_str = str(random.randrange(1,60))
        minuto_fill = minuto_str.zfill(2)
        segundo_str = str(random.randrange(1,60))
        segundo_fill = segundo_str.zfill(2)

        hora_gerada = hora + minuto_fill + segundo_fill

    return hora_gerada


def gera_transacao():
    cliente_data = sorteia_cliente() #sorteia um cliente aleatório dentro da base dados, e armazena todos os dados em forma de lista;
    estabelecimento_data = sorteia_estabelecimento() #sorteia um estabelecimento aleatório dentro da base de dados, e armazena todos os dados em forma de lista;
    id_transacao = gera_id_transacao() #gera uma ID para a transação que está sendo criada (sha256)
    nome_cliente = cliente_data[0][2] #acessa a variável cliente_data e retorna o nome do cliente;
    nome_estabelecimento = estabelecimento_data[0][1] #acessa a variável estabelecimento_data e retorna o nome do estabelecimento;
    tipo_estabelecimento = estabelecimento_data[0][4] #acessa a variável estabelecimento_data e retorna o tipo do estabeelcimento;
    valor_transacao = gera_valor_transacao() #gera um valor do tipo float para a transação que está sendo criada;
    local_transacao = estabelecimento_data[0][3] #acessa a variável estabelecimento_data e retorna o local do estabelecimento;
    numero_aleatorio = random.randrange(1,101) #número responsável por definir (weighted choice) se a transação será bem sucedida ou fraudulenta;
    data_transacao = gera_data_transacao() #gera uma data para a transação que está sendo criada (YYYY-MM-DD);
    hora_transacao = gera_hora_transacao() #gera um horário para a transação que está sendo crada (HH:MM:SS);


    if (numero_aleatorio >=1 and numero_aleatorio <=5):

        numero_aleatorio_fraude = random.randrange(0,2)

        situacao_transacao = "No"
        motivo_transacao_lista = ["Senha Bloqueada", "Saldo Insuficiente"]
        motivo_transacao = motivo_transacao_lista[numero_aleatorio_fraude]

        conexao = mysql.connector.connect(host="localhost",user="root",password="DEcimasenha@883!",database="sistema_transacional")

        cursor = conexao.cursor()

        sql = ("INSERT INTO tab_transacoes (ID, NOME_CLIENTE, NOME_ESTABELECIMENTO, TIPO_ESTABELECIMENTO, VALOR, LOCAL_TRANSACAO, SITUACAO, MOTIVO, YYYY_MM_DD, HORA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_sql = (id_transacao, nome_cliente, nome_estabelecimento, tipo_estabelecimento, valor_transacao, local_transacao, situacao_transacao, motivo_transacao, data_transacao, hora_transacao)

        cursor.execute(sql, data_sql)

        conexao.commit()

    else:

        situacao_transacao = "Ok"
        motivo_transacao = "Sucesso"

        conexao = mysql.connector.connect(host="localhost",user="root",password="DEcimasenha@883!",database="sistema_transacional")

        cursor = conexao.cursor()

        sql = ("INSERT INTO tab_transacoes (ID, NOME_CLIENTE, NOME_ESTABELECIMENTO, TIPO_ESTABELECIMENTO, VALOR, LOCAL_TRANSACAO, SITUACAO, MOTIVO, YYYY_MM_DD, HORA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_sql = (id_transacao, nome_cliente, nome_estabelecimento, tipo_estabelecimento, valor_transacao, local_transacao, situacao_transacao, motivo_transacao, data_transacao, hora_transacao)

        cursor.execute(sql, data_sql)

        conexao.commit()


# código
n_execucoes = 200

for i in range(n_execucoes):

    gera_transacao()
