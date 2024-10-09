#frase = str(input(print("Ingrese una frase: ")))
frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
palabra = str(input(print("Ingrese una palabra: ")))

txtList = frase.replace(".", " ").replace(", ", " ").split()

total = 0

#txtList = frase.split(", ")
#newFrase = []

#for elem in txtList:
#    newFrase.append(elem.split())

print(txtList)

for elem in txtList:
    #for word in elem:
    if elem.lower() == palabra:
       total +=1

print(total)