tabla = {("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
         ("D", "G"): 2,
         ("B", "C", "M", "P"): 3,
         ("F", "H", "V", "W", "Y"): 4,
         ("K"): 5,
         ("J", "X"): 8,
         ("Q", "Z"): 10}


def esLetra(char):
    return (char.lower() >= "a" and char.lower() <= "z")


texto = str(input("Ingrese una palabra: "))
palabra = texto.replace("á" or "Á", "a").replace("é" or "É", "e").replace("í" or "Í", "i").replace("ó" or "Ó", "o").replace("ú" or "Ú", "u")
print(palabra)
puntos = 0

for elem in palabra:
    if esLetra(elem):
        for clave in tabla:            
            if elem.upper() in clave:
                puntos += tabla[clave]

print(f"Puntos: {puntos}")