def string_revert(text):
    resp = None
    try:
        resp = ""
        if type(text) != str:
            raise Exception("O valor passado não é um texto!")
        current_index = len(text)-1

        while current_index >= 0:
            resp += text[current_index]
            current_index -= 1 
        return resp       
    except Exception as error:
        resp = error
    return resp

print(string_revert("Wellington"))