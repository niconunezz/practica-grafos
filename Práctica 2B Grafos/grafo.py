from cola import Cola

class GrafoMA:
    def __init__(self, num_vertices, dirigido):
        self.__num_vertices = num_vertices
        self.__num_aristas = 0
        self.__dirigido = dirigido
        self.__matriz_ady = [[False] * self.__num_vertices for _ in range(self.__num_vertices)]

    # =================================================================================== #
    # Métodos de acceso y checks
    # =================================================================================== #

    def get_dirigido(self):
        return self.__dirigido

    def get_num_vertices(self):
        return self.__num_vertices

    def vertice_en_rango(self, vertice):
        return 0 <= vertice < self.__num_vertices

    def get_numero_aristas(self):
        return self.__num_aristas

    # ==================================================================================== #
    # Métodos de acceso a la matriz de adyacencia
    # ==================================================================================== #

    def existe_arista(self, origen, destino):
        if not self.vertice_en_rango(origen):
            print(f"Error, el vertice {origen} está fuera de rango")
            return
        
        if not self.vertice_en_rango(destino):
            print(f"Error, el vertice {destino} está fuera de rango")
            return

        return self.__matriz_ady[origen][destino]

    def insertar_arista(self, origen, destino):
        if not self.vertice_en_rango(origen):
            print(f"Error, el vertice {origen} está fuera de rango")
            return
        
        if not self.vertice_en_rango(destino):
            print(f"Error, el vertice {destino} está fuera de rango")
            return

        if self.existe_arista(origen, destino):
            print(f"Error, la arista con origen en {origen} y destino en {destino} ya existe")
            return

        self.__matriz_ady[origen][destino] = True
        self.__num_aristas += 1

        if not self.get_dirigido() and destino != origen:
            self.__matriz_ady[destino][origen] = True
            self.__num_aristas += 1

    def elimina_arista(self, origen, destino):
        if not self.vertice_en_rango(origen):
            print(f"Error, el vertice {origen} está fuera de rango")
            return
        
        if not self.vertice_en_rango(destino):
            print(f"Error, el vertice {destino} está fuera de rango")
            return

        if not self.existe_arista(origen, destino):
            print(f"Error, la arista con origen en {origen} y destino en {destino} no existe")
            return
        
        self.__matriz_ady[origen][destino] = False
        self.__num_aristas -= 1

        if not self.get_dirigido() and destino != origen:
            self.__matriz_ady[destino][origen] = False
            self.__num_aristas -= 1

    # ==================================================================================== #
    # Métricas de vértice
    # ==================================================================================== #

    def grado_entrada(self, vertice):
        if not self.vertice_en_rango(vertice):
            return 0
        return sum(self.__matriz_ady[i][vertice] for i in range(self.__num_vertices))

    def grado_salida(self, vertice):
        if not self.vertice_en_rango(vertice):
            return 0
        return sum(self.__matriz_ady[vertice])

    def incidencia(self, vertice):
        result = 0
        if self.vertice_en_rango(vertice):
            if not self.get_dirigido():
                result = self.grado_entrada(vertice) + self.grado_salida(vertice)
            else:
                result = self.grado_entrada(vertice) - self.grado_salida(vertice)
        return result

    # ==================================================================================== #
    # Métodos de recorrido
    # ==================================================================================== #

    def __inicia_visitados(self):
        return [False] * self.__num_vertices

    def recorrido_en_profundidad(self):
        """Recorre todos los vértices del grafo en profundidad."""
        visitados = self.__inicia_visitados()
        for i in range(self.__num_vertices):
            if not visitados[i]:
                self.recorrido_en_profundidad_desde_vertice(i, visitados)

    def recorre_profundidad_cadena(self, vertice, visitados, imprimir):
        """Recorrido en profundidad de una componente conexa de un grafo dirigido."""
        visitados[vertice] = True
        if imprimir:
            print(f"{vertice} ", end="")
        for i in range(self.__num_vertices):
            if (self.existe_arista(vertice, i) or self.existe_arista(i, vertice)) and not visitados[i]:
                self.recorre_profundidad_cadena(i, visitados, imprimir)

    def recorrido_amplitud(self):
        """Recorre todas las componentes del grafo en amplitud."""
        visitados = self.__inicia_visitados()
        for i in range(self.__num_vertices):
            if not visitados[i]:
                self.recorrido_amplitud_desde_vertice(i, visitados)
        print()
    
    def es_grafo_conexo(self):
        """Determina si un grafo es conexo."""
        visitados = self.__inicia_visitados()
        if self.get_dirigido():
            self.recorre_profundidad_cadena(0, visitados, False)
        else:
            self.recorrido_en_profundidad_desde_vertice(0, visitados)
        return all(visitados)

    # ==================================================================================== #
    # Métodos modificados para la práctica
    # ==================================================================================== #

    def recorrido_en_profundidad_desde_vertice(self, vertice, visitados=None, imprimir=False):
        """Realiza un recorrido en profundidad del grafo a partir del vértice especificado."""
        if visitados is None:
            visitados = self.__inicia_visitados()

        visitados[vertice] = True
        #Modificación para no siempre imprimir.
        if imprimir:
            print(f"{vertice} ", end="")
        for i in range(self.__num_vertices):
            if self.existe_arista(vertice, i) and not visitados[i]:
                self.recorrido_en_profundidad_desde_vertice(i, visitados)

    def recorrido_amplitud_desde_vertice(self, vertice):
        """
        Realiza un recorrido en amplitud desde un vértice y calcula
        los saltos mínimos (distancia en aristas) a cada vértice alcanzable.

        Args:
            vertice: índice del vértice desde el cual comenzar el recorrido.

        Returns:
            Una lista con los saltos desde el vértice dado a cada otro vértice.
            Si un vértice no es alcanzable, su valor será -1.
        """
        saltos = [-1] * self.__num_vertices
        cola = Cola()
        cola.encolar(vertice)
        saltos[vertice] = 0

        while not cola.vacia():
            actual = cola.desencolar()
            for i in range(self.__num_vertices):
                if self.existe_arista(actual, i) and saltos[i] == -1:
                    saltos[i] = saltos[actual] + 1
                    cola.encolar(i)

        return saltos



    # ==================================================================================== #
    # Métodos para mostrar el grafo por pantalla
    # ==================================================================================== #

    def mostrar(self):
        print(f"El Grafo tiene una Matriz de {self.__num_vertices} x {self.__num_vertices}")
        if self.get_dirigido():
            print("De un Grafo Dirigido")
        else:
            print("De un Grafo No Dirigido")
        for i in range(self.__num_vertices):
            for j in range(self.__num_vertices):
                print(" T " if self.__matriz_ady[i][j] else " F ", end="")
            print()

    def mostrar_ampliado(self):
        """Imprime la matriz por consola con números en las filas y columnas si es menor de 10 vértices."""
        print(f"El Grafo tiene una Matriz de {self.__num_vertices} x {self.__num_vertices}")
        if self.get_dirigido():
            print("De un Grafo Dirigido")
        else:
            print("De un Grafo No Dirigido")
        if self.__num_vertices < 10:
            print("   ", end="")
            for ele in range(self.__num_vertices):
                print(f" {ele} ", end="")
            print()
        for i in range(self.__num_vertices):
            if self.__num_vertices < 10:
                print(f" {i} ", end="")
            for j in range(self.__num_vertices):
                print(" T " if self.__matriz_ady[i][j] else " F ", end="")
            print()
            

