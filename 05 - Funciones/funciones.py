def es_primo(primo):
    mitad = primo /2
    esPrimo = "Es primo"
    for i in range(2,primo):
        if primo % i == 0:
            esPrimo = "No es primo"
    return esPrimo

print(es_primo(4))