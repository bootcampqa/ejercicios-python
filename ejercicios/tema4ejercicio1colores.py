def colormensaje(color):
    if color == "rojo":
        mensaje = "mensaje de pasión y energía"
    elif color == "verde":
        mensaje = "mensaje de esperanza y crecimiento"
    elif color == "azul":
        mensaje = "mensaje de calma y serenidad"
    elif color == "amarillo":
        mensaje = "mensaje de felicidad y optimismo"
    elif color == "morado":
        mensaje = "mensaje de sabiduría y creatividad"
    else:
        mensaje = "color incorrecto, intente de nuevo"
    return mensaje


def main():
    # Pedimos al usuario que elija un color
    color = input("Elige un color: ")
  
    print(colormensaje(color))


main()