relatorios = {
    "Relatório de vendas 2020": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020"
}
try:
    print(relatorios["Relatório de vendas 2020"])
except KeyError:
    print("Relatório não indentificado")

print(None)
