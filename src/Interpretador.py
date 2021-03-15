import jellyfish as jf
from Relatorio import Relatorio
from app import app
class Interpretador:

    def __init__(self, desejoUsuario):
        self.desejoUsuario = desejoUsuario

    def __str__(self):
        return "Objeto '{0}' da classe Interpretador".format(self.desejoUsuario)

    
    def calcular_grau_de_similaridade_frases(self, nomeRelatorio):
        """calcula o grau de simililaridade entre duas frases, o desejo do 
        usuario e nome do relatorio disponivel"""
        resultadoComparacao = float(jf.levenshtein_distance(
            self.desejoUsuario, 
            nomeRelatorio))
        return resultadoComparacao

    def procurar_relatorio_satisfatorio(self):
        relatorio = Relatorio() 

        #setando indices para auxiliar na busca
        listaRelatorio = []
        listaComandos = []
        listaLevenshtein = []
        #item[0] = nome do relatorio
        #item[1] = select para gerar o relatorio
        for item in relatorio.listaRelatorios.items():
            listaRelatorio.append(item[0])
            listaComandos.append(item[1])
            listaLevenshtein.append(self.calcular_grau_de_similaridade_frases(item[0]))
        
        #procurar relatorio mais similiar
        value, indice = min((val, idx) for (idx, val) in enumerate(listaLevenshtein))
        app.logger.debug("Pontuação: {0}, Desejo: {1}, Encontrado: {2}, Comando: {3}".format(
            value, 
            self.desejoUsuario, 
            listaRelatorio[indice],
            listaComandos[indice]))

        return listaComandos[indice]


