def maiusculas(frase):
    letras_M = ""
    for i in range(len(frase)):
        if 65 <= ord(frase[i]) <= 90:
            letras_M += frase[i]
    return letras_M
