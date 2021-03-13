import spacy
nlp = spacy.load('pt_core_news_sm')
#doc = nlp(u'Você encontrou o lindo livro 01 em estado novo que eu te falei, Carla?')
#doc = nlp(u'O primeiro uso de desobediência civil em massa ocorreu em setembro de 1906.')
doc = nlp(u'Gerar relatorio de vendas de 2020')
print(doc.text.split())
print([token for token in doc])
print([(token.orth_, token.pos_) for token in doc])