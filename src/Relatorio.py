class Relatorio:

    def __init__(self, 
        listaRelatorios = {
        "Relatório de vendas 2020": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020",
        "Relatório de vendas 2019": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020",
        "Relatório de vendas 2018": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020"
        }):
        self.listaRelatorios = listaRelatorios
        

rela = Relatorio()
print(rela.listaRelatorios)