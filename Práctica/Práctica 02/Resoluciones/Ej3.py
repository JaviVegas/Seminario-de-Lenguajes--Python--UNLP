#Para poder checkear si es string o no.
import string

jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

#Creo una lista donde guardo como elementos cada palabra de "jupyter_info".
txtList = jupyter_info.split()

#Leo un caracter desde teclado.
char = str(input("Ingrese una letra: "))

#Si el caracter ingresado es una letra,
#  -> Para cada elemento de la lista,
#    -> Si la palabra empieza con la letra ingresada (forzada a minúscula para ),
#      -> Imprimo la palabra.
if char in string.ascii_letters:
    for elem in txtList:
        if elem.lower().startswith(char.lower()):
            print(elem)

#Si no es una letra,
#  -> Imprimo un mensaje de error            
else:
    print("[!] El caracter ingresado no es una letra.")