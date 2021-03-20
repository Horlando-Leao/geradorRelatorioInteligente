from datetime import *

from MysqlDataBase import MysqlDataBase
from Interpretador import Interpretador
from Util import Util

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
        consulta = MysqlDataBase(database="desafio_a10")

        sql = Inter.procurar_relatorio_satisfatorio()
        print(sql)

        temParametros = consulta.executarSql("select temParameto from relatorios where comando = '{0}'".format(sql))#consulta se o comando sql recebe parametros
        temParametros = temParametros[0][0][0]
        print("1 para tem e 0 para não: ",temParametros)

        if(int(temParametros) == 1 and Util().procurarStrings(True, Inter.desejoUsuario, ['POR ANO', 'DO ANO']) ):#verifica se o comando sql tem parametros e se é de data
            parametroAno = Inter.indetificar_parametos_ano()#pega todas as datas no desejo do usuário
            print('tem parâmetro', parametroAno)

            if(len(parametroAno) == 2):#duas datas
                print("Tem 2 datas")
                a1, m1, d1 = [int(x) for x in parametroAno[0].split('-')] 
                a2, m2, d2 = [int(x) for x in parametroAno[1].split('-')] 
                data1 = date(a1, m1, d1)
                data2 = date(a2, m2, d2)
                if data1 == data2: 
                    print("AS datas são iguais") 
                    sql = sql + " = '{0}';".format(str(data1))

                elif data1 > data2: 
                    print("A primeira data é maior") 
                    sql = sql + " between '{1}' and '{0}' ;".format(str(data1), str(data2))

                else: 
                    print("a segunda data é maior")
                    sql = sql + " between '{0}' and '{1}' ;".format(str(data1), str(data2))
            elif(len(parametroAno) == 1):#um data
                print("Tem 1 datas")
                sql = sql + " = '{0}';".format(str(parametroAno[0]))

            
            #sql = sql + " >'{0}'".format(str(parametroAno[0]))
        else:
            sql = sql
            print("Não tem parâmetro ", temParametros)
        
        """agora só preciso alterar o serviço para que alem de indetificar o nome do relatorio
        que o usuário tem intenção de obter também setar parametros de restrinção na clasura where do sql
        que está previamente gravado em uma tabela no banco"""

        print(sql)
        listaJson = consulta.selectJson(sql)
    
        return listaJson

""" novoServico = Services()
print(novoServico.gerarRelatorio("Relatorio de vendas por ano 2017 a 2020 "))
print(novoServico.gerarRelatorio("Relatorio de vendas por ano 2020 a 2020 "))
print(novoServico.gerarRelatorio("Relatorio de vendas por ano 2020 "))
print(novoServico.gerarRelatorio("Relatorio de vendas")) """
