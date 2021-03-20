from unidecode import unidecode
import spacy

from Util import Util

nlp = spacy.load('pt_core_news_sm')

class IdentificarParametros:
    def __init__(self, desejoUsuario):
        self.desejoUsuario = desejoUsuario

    def indetificarParametosAno(self):
        """Retorna uma array de string que contém datas"""
        desejoUsuarioTratado = nlp(unidecode(self.desejoUsuario.upper()))
        #print(desejoUsuarioTratado)

        tokensDesejo = ([(token.orth_, token.pos_) for token in desejoUsuarioTratado])
        #print(tokensDesejo)

        listaTokensNum = []
        for items in tokensDesejo:
            #items[0] string token
            #items[1] id do tipo toke
            if(items[1] == "NUM" and len(items[0]) == 4):#numero e ano inteiro 2020
                listaTokensNum.append("01-01-" + str(items[0]))

            elif(items[1] == "NUM" and len(items[0]) == 2):#numero e ano encurtado 20
                listaTokensNum.append("01-01-20" + str(items[0]))


        #print(listaTokensNum)

        listaDatas =[]
        for datas in listaTokensNum:
            #print(datas)
            expresaoData = Util.detectarDataExpressaoRegular(str(datas))
            listaDatas.append(expresaoData[0])
        return listaDatas

        


""" idP = IdentificarParametros("relatório 2020 18")
print(idP.indetificarParametosAno()) """