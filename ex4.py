#Vou tratar os dados fornecidos como dicionários
lista = [
    {
        "estado": "SP",
        "faturamento": 67836.43
    },
    {
        "estado": "RJ",
        "faturamento": 36678.66
    },
    {
        "estado": "MG",
        "faturamento": 29229.88
    },
    {
        "estado": "ES",
        "faturamento": 27165.48
    },
    {
        "estado": "Outros",
        "faturamento": 19849.53
    }
]

def get_total_profit(list):
    total_profit = 0
    for estado in list:
        total_profit += float(estado["faturamento"])
    return total_profit

def get_state_relevance(list):
    total = get_total_profit(list)

    for estado in list:
        estado["porcentagem"] = f"{100 * float(estado['faturamento']) / float(total)} %"
    return list

print(get_state_relevance(lista))