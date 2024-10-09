evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

txtList = evaluar.split()
titulo = []

pos = 0
elem = txtList[pos]

#Mientras la palabra actual no sea la última del titulo,
#  -> La agrego a la lista, aumento en 1 el valor de la pos, y me posiciono en la sig palabra.
while elem != "resumen:":
    titulo.append(elem)
    
    pos += 1
    elem = txtList[pos]
    #print(elem)

#print(titulo)

#-------------------------------------------------------------------------

facil = 0; aceptable = 0; dificil = 0; muyDificil = 0
resumen = []

#Mientras no llegue al último elemento,
while pos +1 <= len(txtList):
    oracion = []

    #  -> Mientras la palabra actual no sea la última de la oración,
    #    -> La agrego a la lista, aumento en 1 el valor de la pos, y me posiciono en la sig palabra.
    while not elem.endswith("."):        
        oracion.append(elem)
                
        elem = txtList[pos]
        pos += 1

    oracion.append(elem)  #Guardo la última palabra de la oracion porque sale del while sin guardarla, por tener un punto.
    resumen.append(oracion)  #Guardo la lista "oracion" como sub-lista de "resumen".

    #Si no llegué al final,
    # -> Me muevo al inicio de la sig oracion.
    if pos < len(txtList):
        elem = txtList[pos]
        pos += 1

#-------------------------------------------------------------------------

#Sumo sobre las variables dependiendo de la longitud de cada sub-lista "oracion" dentro de la lista "resumen".
for item in resumen:
    
    if len(item) <= 12:
        facil += 1
    elif len(item) <= 17:
        aceptable += 1
    elif len(item) <= 25:
        dificil += 1
    else:
        muyDificil += 1


if len(titulo)-1 <= 10:
    print("Titulo: Ok")
    facil += 1
else:
    print("  [!] El titulo supera las 10 palabras.")

print("Cantidad de oraciones fáciles de leer: ", facil, ", aceptables para leer: ", aceptable, ", dificil de leer: ", dificil, ", muy difícil de leer: ", muyDificil)