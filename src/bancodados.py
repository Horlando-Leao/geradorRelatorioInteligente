class BancoDados:
test.
    def __init__(self, nomeConexao):
        self.nomeConexao = nomeConexao

    def __str__(self):
        return "Objeto '{0}' da classe BancoDados".format(self.nomeConexao)

novaC = BancoDados("conexao mysql")
print(novaC)

