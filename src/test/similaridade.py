def levenshtein(s1, s2):
    # nas duas linhas abaixo asseguramos que 2 strings devem ser passadas por paramêtro
    assert isinstance(s1, str), "s1 isn't a string"
    assert isinstance(s2, str), "s2 isn't a string"
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    """Vamos calcular todas as linhas e colunas da matriz, para
    obtermos os valores mínimos de cada operação
    """
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Cálculo da inserção na posição j + 1 mais custo de 1
            insertions = previous_row[j + 1] + 1
            # Cálculo da deleção na posição j mais custo de 1
            deletions = current_row[j] + 1
            # Cálculo da substituição na posição j + 1 mais custo de 1 caso a substituição ocorra. Caso não ocorra, o custo é 0
            substitutions = previous_row[j] + (c1 != c2)
        # Recuperamos o menor valor das 3 operações e salvamos no
        current_row 
   
        current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


print(levenshtein('rato', 'gato'))