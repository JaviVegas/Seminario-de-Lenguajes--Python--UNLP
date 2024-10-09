from random import choice, randrange
from datetime import datetime

# Operadores posibles.
operators = ["+", "-", "*", "/"]

# Cantidad de cuentas a resolver.
times = 5

# Contador inicial de tiempo.
# Esto toma la fecha y hora acutal.
init_time = datetime.now()

# Contadores de resultados correctos e incorrectos.
cant_correctos = 0
cant_incorrectos = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range(0, times):
    # Se eligen numeros y operador al azar.
    number_1 = randrange(10)
    number_2 = randrange(10)    
    operator = choice(operators)
    
    # Dependiendo del operador elegido, se obtiene la respuesta correcta a la operación.
    match operator:
        case "+":
            answer = number_1 + number_2            

        case "-":
            answer = number_1 - number_2

        case "*":            
            answer = number_1 * number_2            
        
        case "/":
            # Mientras el divisor sea igual a 0
            # Lo cambiamos por otro valor para evitar dividir por 0.            
            while number_2 == 0:
                number_2 = randrange(10)
                
            answer = number_1 / number_2
            answer = int(answer * 10) / 10

    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuanto es {number_1} {operator} {number_2}?")

    # Le pedimos al usuario el resultado.
    result = float(input("Resultado: "))

    # Informamos al usuario si su respuesta fue correcta o incorrecta.
    if result == answer:
        print("¡Correcto!")
        cant_correctos += 1

    else:
        print(f"Incorrecto... la respuesta era {answer}.")
        cant_incorrectos += 1


# Al terminar toda la cantidad de cuentas por resolver
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos el tiempo transcurrido en segundos
# Junto con la cantidad total de respuestas correctas e incorrectas.
print("\n **************************")
print(f" ¡Tardaste {total_time.seconds} segundos!")
print(f" Respuestas Correctas: {cant_correctos}")
print(f" Respuestas Incorrectas: {cant_incorrectos}")
print(" ************************** \n")