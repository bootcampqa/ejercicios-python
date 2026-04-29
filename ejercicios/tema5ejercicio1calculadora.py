
def calcularmedia(cantNotas):
    suma = 0

    for i in range(cantNotas):
        valor = int(input("Ingrese nota: "))
        suma = suma + valor
   
    media = suma/cantNotas

    return media;


def calculadora ():
    print("Calculadora de nota media")
    cantNotas = int(input("¿Cuántas notas desea introducir?: "))

    media = calcularmedia(cantNotas)


    print("Media " + str(media))

    print("Media", media)

calculadora()



