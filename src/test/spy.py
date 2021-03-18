from detectarData import date_detector
import spacy
nlp = spacy.load('pt_core_news_sm')
#doc = nlp(u'Você encontrou o lindo livro 01 em estado novo que eu te falei, Carla?')
#doc = nlp(u'O primeiro uso de desobediência civil em massa ocorreu em setembro de 1906.')
doc = nlp(u'Gerar relatorio de vendas de 2020 e 20')
#print(doc.text.split())
#print([token for token in doc])
myTokens = ([(token.orth_, token.pos_) for token in doc])

listaTokensNum = []
for items in myTokens:
    if(items[1] == "NUM" ):
        listaTokensNum.append(items[0])

#print(listaTokensNum)

date_detector("{0}".format(listaTokensNum[0]))

dia ="01"
a= date_detector("{0}-{1}".format(dia, listaTokensNum[0]))
print(a)

ano = 19
for x in range(2):
    a = date_detector("01-01-{0}{1}".format(ano, listaTokensNum[0]))
    print(a)
    ano += 1

ano = 19
for x in range(2):
    a = date_detector("01-01-{0}".format( listaTokensNum[0]))
    print(a)
    ano += 1

lista2020 = [2020,20]
lista2019 = [2019,20]
print(lista2020)