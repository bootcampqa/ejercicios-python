#Hay una tienda con camisetas a 10 euros, gorras a 2 euros y pulseras a 3 euros. 
#Si se llevan más de 2 camisetas, se le hace un descuento de 2 euros.
#Si tiene carnet joven se le hace un descuento de 5 euros.

#Se debe pedir al usuario que indique el numero de camisetas, gorras y pulseras que quiere, y tambien que indique si tiene carnet joven o no para aplicar el descuento.
#Se debe mostrar el precio total de la compra con el descuento aplicado.

def calcular_total_compra(numero_camisetas,numero_gorras,numero_pulseras):
    precio_camiseta = 10
    precio_gorras = 2
    precio_pulseras = 3
    total_compra = (numero_camisetas * precio_camiseta) + (numero_gorras * precio_gorras) + (numero_pulseras * precio_pulseras)
    return total_compra

def aplicar_descuento_camisetas(numero_camisetas,total_compra):
    descuento_camisetas = 2
    if numero_camisetas >= 2:
        total_compra = total_compra - descuento_camisetas
    return total_compra

def aplicar_descuento_carnet(total_compra,tiene_carnet_joven):
    descuento_carnet_joven=5
    if tiene_carnet_joven == "S":
        total_compra = total_compra - descuento_carnet_joven;
    return total_compra

def comprar_camisetas():
   
    numero_camisetas = int( input("Cuantas camisetas quiere "))
    numero_gorras = int(input ("Cuantas gorras quiere "))
    numero_pulseras = int(input ("Cuantas pulseras quiere "))

    tiene_carnet_joven = input("Tiene carnet joven? Indique S o N")


    total_compra = calcular_total_compra(numero_camisetas,numero_gorras,numero_pulseras)

    total_compra = aplicar_descuento_camisetas(numero_camisetas,total_compra)
    
    total_compra = aplicar_descuento_carnet(total_compra,tiene_carnet_joven)
   

    print("El total de la compra es ", total_compra)


comprar_camisetas()

