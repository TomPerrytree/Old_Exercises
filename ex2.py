def fibonacci(tamanho):
    resp = None
    try:
        resp = []
        
        if (type(tamanho) == int) == False:
            raise Exception("Valor passado não é um número!")
        while len(resp) < tamanho:
            if len(resp) < 2:
                resp.append(1)
            else:
                last_index = len(resp)-1
                previous_index = last_index-1
                current_num = resp[last_index] + resp[previous_index]
                resp.append(current_num)
    except Exception as error:
        resp = error
    return resp

def exercicio(num):
    resp = None
    try:
        if type(num) != int:
            raise Exception("Valor passado não é um número")
        sequence = fibonacci(100) #Criando uma sequência grande o suficiente
        for i in range(len(sequence)):
            if num == sequence[i]:
                resp = f"O valor {num} está na sequência de Fibonnaci, sendo ele o {i+1}º número!"
                break
            resp = f"O valor {num} não pertence à sequência de Fibonnaci"
    except Exception as error:
        resp = error
    return resp

print(exercicio(5))
print(exercicio(9))