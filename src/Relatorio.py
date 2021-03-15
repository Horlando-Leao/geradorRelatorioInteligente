class Relatorio:

    def __init__(self, 
        listaRelatorios = {
        "Relatório de vendas 2020": "select valor, ano from vendas where ano >  date('2019-12-31') and ano < date('2021-01-01')",
        "Relatório de vendas 2019": "select valor, ano from vendas where ano >  date('2018-12-31') and ano < date('2020-01-01')",
        "Relatório de vendas 2018 à 2019": "select valor, ano from vendas where ano >  date('2017-12-31') and ano < date('2020-01-01')",
        "Relatório de vendas 2018 à 2020": "select valor, ano from vendas where ano >  date('2017-12-31') and ano < date('2021-01-01')",
        "Relatório de vendas 2015 à 2020": "select valor, ano from vendas where ano >  date('2014-12-31') and ano < date('2020-01-01')",
        "Relatório de vendas 2018": "select valor, ano from vendas where ano >  date('2017-12-31') and ano < date('2019-01-01')",
        "Relatório de vendas": "select valor, ano from vendas"
        }):
        self.listaRelatorios = listaRelatorios
        

""" rela = Relatorio()
print(rela.listaRelatorios) """