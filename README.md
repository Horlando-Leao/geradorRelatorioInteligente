# geradorRelatorioInteligente

## Iniciativa de criar um backend de relatório inteligente.

## O proposito:
O usuário fornecer uma intenção de dados, exemplo "Relatorio de vendas por ano de 2020". 
onde [vendas] = é um desejo, 
[por ano] = é um parâmetro, 
e [2020] é um parâmetro de restrição.

O como óbvio é um problema de PLN pois o usuário não digitara uma síntaxe fixa, o banckend é inteligente suficiente para entender a intenção do usuário.

Como resultado, o backend responde um JSON com os dados filtrados e no frontend renderizar um gráfico

## O que desejo terminar:
Criar uma interface web para inserir os desejos, uma parte do comando slq fixo, e os tipos e quantidades de parametros esperados.
Pretendo criar módulo python(backend) que possa devolver o gráfico para dispositvos moveis para evitar muito processamento em dispositivos movéis.
