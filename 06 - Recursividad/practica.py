def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif (numero % 10 == digito):
        return contar_digito(numero // 10, digito) +1   
    else:
        return contar_digito(numero // 10, digito) 
         
print(contar_digito(23205622, 2))
