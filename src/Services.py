from Relatorio import Relatorio
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
        #print(sql)
        #teste = MysqlDataBase(database="desafio_a10").selectJsonVendas(Interpretador(desejoUsuario).procurar_relatorio_satisfatorio())

        return listaJson

#novoServico = Services().gerarRelatorio("vendas 2020")
#print(novoServico)
#gerarRelatorio("vendas 2020")
