class Nodo:
    def __init__(self, datos, padre=None):   # se cambio a padre en vez de hijo  
        self.datos = datos # se auto escirbia con none
        self.padre = padre # se cambio a padre en vez de none
        self.costo = None
        self.hijos = []  

    def set_hijos(self, hijos):
        self.hijos = hijos  
        if self.hijos is not None:
            for h in hijos:
                h.padre = self

    def get_hijos(self): # estaba llamando a self padre
        return self.hijos

    def get_datos(self): # faltaba este metodo
        return self.datos

    def get_padre(self): # falataba este metodo
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def set_costo(self, costo):
        self.costo = costo

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def __str__(self):
        return str(self.get_datos())

