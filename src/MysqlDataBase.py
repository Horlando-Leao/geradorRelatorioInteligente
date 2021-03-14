import datetime
import mysql.connector
import json

class MysqlDataBase:

    def __init__(self, host="localhost", user="root", password="root", database=None):
        self._host=host
        self._user=user
        self._password=password
        self._database=database

    def getDatabase(self):
        return self._database
    
    def conexaoMysql(self):
        mydb = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database,
            charset='utf8'
        )
        return mydb

    def selectJson(self, sql:str) -> json:
        """consulta sql com retorno em forma de json"""
        mydb = self.conexaoMysql()
        mycursor = mydb.cursor()
        mycursor.execute(sql)

        row_headers=[x[0] for x in mycursor.description]#
        myresult = mycursor.fetchall()

        json_data=[]#
        for result in myresult:#
            json_data.append(dict(zip(row_headers,result)))#
        rs = json.dumps(json_data, ensure_ascii=False).encode('utf8')#

        return rs.decode()

    def selectList(self, sql:str) -> list:
        """consulta sql com retorno em forma de lista"""
        mydb = self.conexaoMysql()
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        
        myresult = mycursor.fetchall()

        dicionario = {}
        for values in myresult:
            dicionario[values[0]] = values[1]

        return dicionario


novaConsulta = MysqlDataBase(database="livraria")
#print(novaConsulta.selectAllJson("SELECT * from livraria.autor"))
lista = (novaConsulta.selectList("SELECT * from livraria.autor"))

print(lista)