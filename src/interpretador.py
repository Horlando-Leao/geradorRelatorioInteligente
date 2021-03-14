import jellyfish as jf

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


    
arg = Interpretador("Relatório de vendas 2020")
print(arg)
print(arg.calcular_grau_de_similaridade_frases("Relatorio de compras 2020"))
