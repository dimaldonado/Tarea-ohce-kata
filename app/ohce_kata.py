def ohce_kata(hora):
    #caso noche
    if(20<=hora<=23):
        return "¡Buenas noches!"
    if(0<=hora<6):
        return "¡Buenas noches!"
    #caso dia
    if(hora==6):
        return "¡Buenos dias!"