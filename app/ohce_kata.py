def ohce_kata(hora):
    #caso noche
    if(20<=hora<=23):
        return "¡Buenas noches!"
    if(0<=hora<6):
        return "¡Buenas noches!"
    #caso dia
    if(6<=hora<12):
        return "¡Buenos dias!"
    #caso tarde
    if(12<=hora<20):
        return "¡Buenas tardes!"
    

def ohce_kata_palindromo(palabra):
    if palabra != palabra[::-1]:
        return palabra[::-1]
     