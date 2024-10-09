import string

texto = """El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas."""

txtList = texto.replace("á", "a").split()

def esPalabra(letra):
    return (letra >= "A" and letra <= "Z") or (letra >= "a" and letra <= "z")

cantMayus = 0
cantMinus = 0
cantNoLetra = 0
cantNoPalabras = 0

for elem in txtList:
    if not esPalabra(elem[0]):
        cantNoPalabras += 1

    for letra in elem:
        if letra >= "A" and letra <= "Z":
            cantMayus += 1
        elif letra >= "a" and letra <= "z":
            cantMinus += 1
        else:
            cantNoLetra += 1

print(f"Mayusculas: ", {cantMayus})
print(f"Minusculas: ", {cantMinus})
print(f"Chars no Letras: ", {cantNoLetra})
print(f"Palabras sin distinguir entre Mayus y Minus: ", {cantNoPalabras})