#Pide a la usuaria un número entre 1 y 10.
#El número ganador es el 4.
#Muestra:
#Mensaje de victoria si acierta.
#Mensaje de derrota si falla.


def ganador(numero):
    numero_ganador = 4
    if numero == numero_ganador:
        print("VICTORIA: el número 4 es el ganador")
    else:
        print("Ha perdido intente de nuevo")
  

def ejercicioganador():
    numero = int(input("Escribe un número entre 1 y 10: "))

    ganador(numero)


ejercicioganador()