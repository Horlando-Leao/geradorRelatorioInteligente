from Relatorio import Relatorio
from Interpretador import Interpretador
from MysqlDataBase import MysqlDataBase


def gerarRelatorio(desejoUsuario="Relatorio"):
    Inter = Interpretador(desejoUsuario)
    novaConsulta = MysqlDataBase(database="desafio_a10")

    sql = (Inter.procurar_relatorio_satisfatorio())
    lista = (novaConsulta.selectList(sql))

    print(sql)
    print(lista)

gerarRelatorio("Relatório 2020")