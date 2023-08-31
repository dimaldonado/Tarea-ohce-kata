import datetime

def ohce_kata_hora(hora,nombre_usuario):
    #caso noche
    if(20<=hora<=23):
        return "¡Buenas noches " + nombre_usuario + "!" 
    if(0<=hora<6):
        return "¡Buenas noches " + nombre_usuario + "!" 
    #caso dia
    if(6<=hora<12):
        return "¡Buenos dias " + nombre_usuario + "!" 
    #caso tarde
    if(12<=hora<20):
        return "¡Buenas tardes " + nombre_usuario + "!" 
    

def ohce_kata_palindromo(palabra):
    if palabra != palabra[::-1]:
        return palabra[::-1]
    else:
        print(palabra[::-1])
        return "¡Bonita palabra!"

def ohce_kata_stop(palabra):
    if palabra =="Stop!":
        return True
    return False

def ohce_kata(hora,nombre_usuario):
    
    print(ohce_kata_hora(hora,nombre_usuario))
    while(True):
        palabra = input()
        if(ohce_kata_stop(palabra)):
            print("Adios " + nombre_usuario)
            exit()
        print(ohce_kata_palindromo(palabra))

if __name__ == "__main__":
    #obtenemos la hora actual
    hora_actual = int(datetime.datetime.now().time().strftime("%H"))
    ohce_kata(hora_actual,"Diego")

    
        


