from Arbol import Nodo

# BFS (búsqueda en amplitud)
def buscar_solucion_BFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)  # FIFO → Cola
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo
        
        # Generar hijos
        dato_nodo = nodo.get_datos()

        hijo_izq = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_cen = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_der = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]

        for hijo in [hijo_izq, hijo_cen, hijo_der]:
            nuevo_nodo = Nodo(hijo, nodo)
            if not nuevo_nodo.en_lista(nodos_visitados) and not nuevo_nodo.en_lista(nodos_frontera):
                nodos_frontera.append(nuevo_nodo)

# DFS (búsqueda en profundidad)
def buscar_solucion_DFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()  # LIFO → Pila
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo
        
        # Generar hijos
        dato_nodo = nodo.get_datos()

        hijo_izq = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_cen = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_der = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]

        for hijo in [hijo_izq, hijo_cen, hijo_der]:
            nuevo_nodo = Nodo(hijo, nodo)
            if not nuevo_nodo.en_lista(nodos_visitados) and not nuevo_nodo.en_lista(nodos_frontera):
                nodos_frontera.append(nuevo_nodo)

# BFS recursivo
def buscar_solucion_BFS_recursivo(nodo, solucion, visitados):
    if nodo.get_datos() == solucion:
        return nodo
    
    visitados.append(nodo.get_datos())

    dato_nodo = nodo.get_datos()

    hijo_izq = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
    hijo_cen = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
    hijo_der = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]

    hijos = [Nodo(hijo_izq, nodo), Nodo(hijo_cen, nodo), Nodo(hijo_der, nodo)]
    nodo.set_hijos(hijos)

    for hijo in nodo.get_hijos():
        if hijo.get_datos() not in visitados:
            sol = buscar_solucion_BFS_recursivo(hijo, solucion, visitados)
            if sol:
                return sol
    return None

# Mostrar el resultado
def mostrar_resultado(nodo_solucion):
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(nodo.get_datos())
        resultado.reverse()
        print("\n")
        for paso in resultado:
            print(paso)
    else:
        print("\n")

# 🚀 Función principal
if __name__ == "__main__":
    estado_inicial = list(map(int, input("Ingresa con espacio los numeros ").split()))
    solucion = list(map(int, input("Ingresa con espacio los numeros ").split()))

    print("\n1. BFS Amplitud")
    print("2. DFS Profundidad")
    print("3. BFS Recursivo")
    opcion = int(input("Seleciona del 1 al 3: "))

    if opcion == 1:
        nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    elif opcion == 2:
        nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    elif opcion == 3:
        nodo_inicial = Nodo(estado_inicial)
        nodo_solucion = buscar_solucion_BFS_recursivo(nodo_inicial, solucion, [])
    else:
        print("Opción no válida")
        exit()

    mostrar_resultado(nodo_solucion)
