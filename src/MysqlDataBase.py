import datetime
import mysql.connector
import json

class MysqlDataBase:

    def __init__(self, host="localhost", user="root", password="root", database=None):
        self.host=host
        self.user=user
        self.password=password
        self.database=database

    def getDatabase(self):
        return self.database
    
    def conexaoMysql(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8'
        )
        return mydb

    def executarSql(self, sql):
        mydb = self.conexaoMysql()
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return [myresult, mycursor]

    def selectList(self, comandoSQL:str) -> list:
        """consulta sql com retorno em forma de lista"""
        myresult = self.executarSql(comandoSQL)

        dicionario = {}
        for values in myresult[0]:
            dicionario[values[0]] = str(values[1])

        return dicionario

    def selectJson(self, comandoSQL:str) -> json:
        """consulta sql com retorno em forma de json"""
        execSql = self.executarSql(comandoSQL)
        row_headers=[x[0] for x in execSql[1].description]#
        myresult = execSql[0]
        
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        resultado = json.dumps(json_data, indent = 2, sort_keys = True, default = str)

        return resultado




""" novaConsulta = MysqlDataBase(database="desafio_a10")
lista = novaConsulta.selectList(comandoSQL="SELECT nome, comando from relatorios") """
#lista = novaConsulta.selectJson(comandoSQL="SELECT idVendas, valor, ano from vendas")
#print(lista)