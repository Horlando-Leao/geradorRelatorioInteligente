from Interpretador import Interpretador
from MysqlDataBase import MysqlDataBase

class Services:

    def __init__(self):
        pass

    def gerarRelatorio(self, desejoUsuario="Relatorio"):
        """Gerar relatorio consiste em interpretar a intenção do usuário, 
        no caso qual relatorio ele deseja buscar o comando sql previamente 
        gravado em uma tabela de dados e colocar se necessário parametros 
        de restrinção na clasura where do sql e desse data set json resgatado 
        no banco, retornar um gráfico qualquer respectivo a inteção do usuário"""

        Inter = Interpretador(desejoUsuario)
        novaConsulta = MysqlDataBase(database="desafio_a10")

        sql = Inter.procurar_relatorio_satisfatorio()
        sql = "sql + parametros se necessario = Inter.indetificar_parametos_ano()"
        """agora só preciso alterar o serviço para que alem de indetificar o nome do relatorio
        que o usuário tem intenção de obter também setar parametros de restrinção na clasura where do sql
        que está previamente gravado em uma tabela no banco"""

        listaJson = novaConsulta.selectJson(sql)
    
        return listaJson

#novoServico = Services().gerarRelatorio("vendas 2020")
#print(novoServico)
#gerarRelatorio("vendas 2020")
