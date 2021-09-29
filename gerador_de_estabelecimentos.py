# importações
import random
import uuid
import hashlib
import mysql.connector


# funções
def gera_id():

    id_gerada = uuid.uuid4()

    id_sha256 = hashlib.sha256()
    id_sha256.update(id_gerada.bytes)

    id_str = id_sha256.hexdigest()
    return id_str

def gera_nome_estabelecimento():

    tipo = ["Farmácia", "Mercado", "Auto Posto", "Clínica", "Cinema", "Loja"]
    nome_estabelecimento = ["São José", "Presidente", "Alagoas", "Carneiro", "Santo Antônio", "Vale", "Multi", "Airos", "Pagen", "Helios", "Hundri", "Gaffi", "Thund"]

    indice_tipo = random.randrange(0, 6)
    indice_nome_estabelecimento = random.randrange(0, 13)

    nome_estabelecimento_gerado = tipo[indice_tipo] + " " + nome_estabelecimento[indice_nome_estabelecimento]
    return nome_estabelecimento_gerado

def gera_endereco():

    tipo_endereco = ["Rua", "Avenida"]
    nome_endereco = ["Manoel Ribas", "Castelo Branco", "Goias", "Central", "Projetada", "Alagoas", "JK", "Raposo Tavares", "Igapó", "Tapajós", "Marechal", "Recintio", "Mamoni", "Getulio", "Kuban", "Fronteira", "Jacinto", "Tempiti", "Sousa", "Naves", "Interventor", "Salin", "Outubro", "Rosas", "Araras", "Tupi", "Virago", "Gertrudes", "Flores", "Beija-Flor", "Sambisti", "Tropa", "Darlene", "Girafas", "Ronald", "Roland"]
    n_endereco = str(random.randrange(11, 2999))

    indice_tipo_endereco = random.randrange(0, 2)
    indice_nome_endereco = random.randrange(0, 36)

    endereco_gerado = tipo_endereco[indice_tipo_endereco] + " " + nome_endereco[indice_nome_endereco] + ", " + n_endereco
    return endereco_gerado

def gera_cidade():

    cidades = ["Rolândia", "Londrina", "Cambé", "Arapongas", "Apucarana", "Ibiporã"]

    indice_cidades = random.randrange(0, 6)

    cidade_escolhida = cidades[indice_cidades]
    return cidade_escolhida


# código
for i in range(48):
    id = gera_id()
    tipo_nome_estabelecimento = gera_nome_estabelecimento()
    endereco = gera_endereco()
    cidade = gera_cidade()

    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DEcimasenha@883!",
    database="sistema_transacional"
    )

    cursor = conexao.cursor()

    sql = ("INSERT INTO tab_estabelecimentos "
        "(ID, NOME, ENDERECO, CIDADE) "
        "VALUES (%s, %s, %s, %s)")
    data_sql = (id, tipo_nome_estabelecimento, endereco, cidade)

    cursor.execute(sql, data_sql)

    conexao.commit()
