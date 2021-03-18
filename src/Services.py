from Interpretador import Interpretador
from MysqlDataBase import MysqlDataBase

class Services:

    def __init__(self):
        pass

    def gerarRelatorio(self, desejoUsuario="Relatorio"):
        Inter = Interpretador(desejoUsuario)
        novaConsulta = MysqlDataBase(database="desafio_a10")

        sql = Inter.procurar_relatorio_satisfatorio()
        listaJson = novaConsulta.selectJson(sql)
    
        return listaJson

#novoServico = Services().gerarRelatorio("vendas 2020")
#print(novoServico)
#gerarRelatorio("vendas 2020")
