
#Función calcular el precio total aplicando descuento e IVA
def calcular_total_producto(precio, cantidad):
    precio_total = precio * cantidad
    return precio_total

def calcular_descuento(total, porcentaje_descuento):
    total_descuento = total - (total * porcentaje_descuento)/100
    return total_descuento

def calcular_IVA(total, iva):
    total_iva = total + (total * iva/100)
    return total_iva


def calcular_operaciones():
    #Solicitud de parámetros al usuario
    nombre_del_producto = input ("¿Cuál es el nombre del producto? ")
    precio_por_unidad = float (input ("¿Cuánto es el precio de una unidad? "))
    cantidad_a_comprar = int (input ("¿Cuántos vas a comprar? "))
    descuento_en_porcentaje = float (input ("¿Qué porcentaje de descuento tiene? "))
    IVA_en_porcentaje = float (input ("¿Qué porcentaje de IVA tiene? "))

    total_compra = calcular_total_producto(precio_por_unidad,cantidad_a_comprar)
    total_descuento = calcular_descuento(total_compra,descuento_en_porcentaje)
    total_iva = calcular_IVA(total_descuento, IVA_en_porcentaje)
    
    print("El total de la compra del producto " + nombre_del_producto + " es ", total_iva, "euros")


calcular_operaciones()