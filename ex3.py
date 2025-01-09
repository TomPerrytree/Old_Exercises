#Eu sei que dá para fazer isso através da leitura de arquivos, no caso do python com open(), porém, vou tratar como um dicionário
amostra_faturamento = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]
def get_min_num(list):
    min = float("inf") #Número infinito que vai reduzindo conforme
    for dia in list:
        '''
        #Versão contando com o zero
        if float(dia["valor"]) < min:
            min = float(dia["valor"])'''
        #Versão ignorando zero!
        if float(dia["valor"]) > 0 and float(dia["valor"]) < min:
            min = float(dia["valor"])
    return min

def get_max_num(list):
    max = float("-inf") #Número infinito que vai reduzindo conforme
    for dia in list:
        '''
        #Versão contando com o zero
        if float(dia["valor"]) > max:
            max = float(dia["valor"])'''
        #Versão ignorando zero!
        if float(dia["valor"]) > max:
            max = float(dia["valor"])
    return max

def get_avg_list(list):
    sum_nums = 0
    total_nums = 0

    for dia in list:
        if float(dia["valor"]) > 0:
            sum_nums += float(dia["valor"])
            total_nums += 1
    return sum_nums / total_nums

def exercicio(list):
    min_num = get_min_num(list)
    max_num = get_max_num(list)
    avg_num = get_avg_list(list)
    better_days = 0

    for dia in list:
        if float(dia["valor"]) > avg_num:
            better_days += 1
    print(f"O menor faturamento do mês foi de R$ {min_num}!")
    print(f"O maior faturamento do mês foi de R$ {max_num}!")
    print(f"{better_days} dias foram superiores à média mensal ({avg_num})!")
exercicio(amostra_faturamento)