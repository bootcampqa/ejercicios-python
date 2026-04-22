#Pide a la usuaria que introduzca la siguiente información sobre su canción favorita.


nombre_cancion = input("Como se llama tu canción favorita? ")

artista = input ("Quién fue el cantante? ")

album = input ("En qué álbum aparece? ")

anyo_lanzamiento = input ("Cual fue el año de lanzamiento? ")

duracion = input ("Cuantos segundos dura la canción ")

tiene_videoclip= input ("Tiene videoclip? ")



nombre_cancion_no_me_gusta = input("Como se llama la canción que menos te gusta? ")

artista_no_gusta = input ("Quién fue el cantante? ")

album_no_gusta = input ("En qué álbum aparece? ")

anyo_lanzamiento_no_gusta = input ("Cual fue el año de lanzamiento? ")

duracion_no_gusta = input ("Cuantos segundos dura la canción ")

tiene_videoclip_no_gusta= input ("Tiene videoclip? ")


print("La canción favorita es " + nombre_cancion + " el artista es " + artista)
print("Album: ", album)
print("Año de Lanzamiento:", anyo_lanzamiento)
print("Duración:", duracion)
print("Tiene Videoclip:", tiene_videoclip)

print("La canción que menos te gusta es " + nombre_cancion_no_me_gusta + " el artista es " + artista_no_gusta)
print("Album: ",album_no_gusta)
print("Año: ",anyo_lanzamiento_no_gusta)
print("Duración: ",duracion_no_gusta)
print("Tiene Videoclip",tiene_videoclip_no_gusta)