
#Creo función con lista meses del año
def meses(introducir_numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[introducir_numero_mes - 1]



# pido a la usuaria número del 1 al 12 devuelvo el mes qué es
def numero_mes():
    introducir_numero_mes = int(input("Introduce un número del 1 al 12: ")) #número del 1 al 12

    if 1 <= introducir_numero_mes <= 12: 
        mes = meses(introducir_numero_mes)    #llamar a la lista de meses
        print(f"El mes número {introducir_numero_mes} es: {mes}") 
        if introducir_numero_mes == 6:  #incluyo otra condición para el mes de junio(6)
         print("El mejor mes del año!")
    else: 
        print("tiene que ser un número entre 1 y 12")
   

numero_mes()
