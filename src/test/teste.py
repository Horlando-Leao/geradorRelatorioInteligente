relatorios = {
    "Relatório de vendas 2020": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020",
    "Relatório de vendas 2019": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020",
    "Relatório de vendas 2018": "select * from vendas where ano > 01/01/2020 abd ano < 31/12/2020"
}

for key in relatorios:
    print(key)
    print(relatorios[key])

listRelatorio = relatorios.items()

for item in relatorios.items():
    print(item[0])

for item in relatorios.items():
    print(item[1])

for item in relatorios.items():
    print(item)

try:
    print(relatorios["Relatório de vendas 2020"])
    print(relatorios["Relatório de vendas 202"])
except KeyError:
    print("Relatório não indentificado")


