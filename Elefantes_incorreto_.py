def  incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    lista_numerica = [x for x in range(n+1, 0, -1)]
    if n < 1:
        return ""
    else:
        if n == 1:
            texto_a = "Um elefantes incomoda muita gente\n"
            return texto_a
        else:
            texto_a = str(n)+" elefantes incomoda muita gente\n"
            texto_b = "muito mais\n"
            return texto_a + str(n) + " elefantes " + incomodam(n) + texto_b + elefantes(n-1)
                       
        
        
