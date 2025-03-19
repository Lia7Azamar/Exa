from flask import Flask, render_template, request
from Puzle_exam import buscar_solucion_BFS, buscar_solucion_DFS, buscar_solucion_BFS_recursivo
from Arbol import Nodo

app = Flask(__name__)

# Funciones de búsqueda ya importadas
def mostrar_resultado(nodo_solucion):
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(nodo.get_datos())  # Agregar el nodo inicial
        resultado.reverse()  # Invertir para mostrar el camino desde el inicio
        return resultado
    else:
        return []

# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario y mostrar resultados
@app.route('/resultados', methods=['POST'])
def resultados():
    # Obtener los datos del formulario
    metodo = int(request.form['metodo'])
    estado_inicial = list(map(int, request.form['estado_inicial'].split()))
    solucion = list(map(int, request.form['solucion'].split()))

    if metodo == 1:
        nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    elif metodo == 2:
        nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    elif metodo == 3:
        nodo_inicial = Nodo(estado_inicial)
        nodo_solucion = buscar_solucion_BFS_recursivo(nodo_inicial, solucion, [])
    else:
        return "Opción no válida", 400

    # Mostrar el resultado
    resultado = mostrar_resultado(nodo_solucion)
    return render_template('resultados.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
