#Lista de planetas


#Función pedir al usuario un número del 1 al 8


#Función mostrar número de la lista
def mostrar_planeta (numero):
    planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
    if numero >=1 and numero <= 8:
        mensaje = planetas [numero -1]
    else: 
        mensaje ="El número introducido no está dentro de rango (1 al 8), vuelve a intentarlo. "

    return mensaje




numero = int (input ("Elige un número del 1 al 8 => "))
    
print(mostrar_planeta (numero))

