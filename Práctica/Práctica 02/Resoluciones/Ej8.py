acentos = ["á", "é", "í", "ó", "ú"]

def esLetra(char):
    esAcento = False    
    for elem in acentos:
        if char == elem:
            esAcento = True

    return (char.lower() >= "a" and char.lower() <= "z") or esAcento


letras = {}

texto = str(input("Ingrese una palabra o frase: "))
actual = 0
sigo = True

while actual < len(texto) and sigo:
    if esLetra(texto[actual]):
        if texto[actual] in letras:
            sigo = False
        else:
            letras[texto[actual]] = 1
  
    actual += 1


if sigo:
    print("Es un Heterograma.")
else:
    print("No es un Heterograma.")