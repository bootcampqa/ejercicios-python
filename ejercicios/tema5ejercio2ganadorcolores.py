#Pedir a la usuaria 5 veces que introduzca un color, Solución

def color():
    for i in range(5):
        color = input ("Introduce un color: ")

        if color == "azul":
            print("¡Has ganado!")
            break;
        else:
            print("¡Prueba otro color!")


#solución alternativa si quereis usar while
def ejemplowhile():
    contador=0
    while color!="azul" and contador < 5:
        contador +=1
        color = input ("Introduce un color: ")

        if color == "azul":
            print("¡Has ganado!")
        else:
            print("¡Prueba otro color!")
    

color()
# Hay algo que no me cuadra en el color porque si lo introduce 5 veces y luego en una de las veces es azul, igualmente sale que pruebe con otro color... 