class Banda():
    
    generos = set()
        
    def __init__(self, nombre, genero="None"):
        self.nombre=nombre
        self.genero=genero
        self._integrantes=[]
        Banda.generos.add(genero)
        
    def get_integrantes(self):
         return self._integrantes
    
    def set_integrantes(self, lista):
         self._integrantes = lista
    
    def __str__(self):
        texto = f"La banda de {self.genero} {self.nombre} está integrada por: "
        for elem in self._integrantes:
            texto += f"\n\t\t{elem}"
        return texto
    
    integrantes = property(get_integrantes, set_integrantes)
