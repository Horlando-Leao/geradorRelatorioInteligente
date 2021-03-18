from MysqlDataBase import MysqlDataBase

class Relatorio:

    def __init__(self):
        pass

    def getListaComandoRelatorio(self):
        novaConsulta = MysqlDataBase(database="desafio_a10")
        lista = novaConsulta.selectList(comandoSQL="SELECT nome, comando from relatorios")
        return lista

    def getExamplesListaComandoRelatorio(self):
        exampleslistaRelatorios = {
        "Relatório de clientes 2020": "select valor, ano from vendas where ano >  date('2019-12-31') and ano < date('2021-01-01')",
        "Relatório de vendas 2019": "select valor, ano from vendas where ano >  date('2018-12-31') and ano < date('2020-01-01')",
        "Relatório de vendas 2018 à 2019": "select valor, ano from vendas where ano >  date('2017-12-31') and ano < date('2020-01-01')",
        "Relatório de vendas 2018 à 2020": "select valor, ano from vendas where ano >  date('2017-12-31') and ano < date('2021-01-01')",
        "Relatório de vendas 2015 à 2020": "select valor, ano from vendas where ano >  date('2014-12-31') and ano < date('2020-01-01')",
        "Relatório de vendas 2018": "select valor, ano from vendas where ano >  date('2017-12-31') and ano < date('2019-01-01')",
        }
        return exampleslistaRelatorios

""" rela = Relatorio().getListaComandoRelatorio()
print(rela) """