class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono



class GrafoMA:
    def __init__(self, size: int, dirigido: bool):
        self._size = size
        self._dirigido = dirigido
        self._numAristas = 0
        self._matriz_ady = [[False]*self._size for _ in range(self._size)]

    def get_dirigido(self):
        return self._dirigido
    
    def get_num_vertices(self):
        return self._size
    
    def vertice_en_rango(self, vertice):
        return vertice<self._size and vertice >= 0
    
    def existe_arista(self, origen, destino):
        if self.vertice_en_rango(origen) and self.vertice_en_rango(destino):
            return self._matriz_ady[origen][destino]
    
    def insertar_arista(self, origen, destino):
        if self.vertice_en_rango(origen) and self.vertice_en_rango(destino):
            self._numAristas += 1
            self._matriz_ady[origen][destino] = 1

    def grado_entrada(self, vertice):
        # sum([True, True, False, True]) = 3
        if self.vertice_en_rango(vertice):
            return sum(self._matriz_ady[:, vertice])
    
    def grado_salida(self, vertice):
        # sum([True, True, False, True]) = 3
        if self.vertice_en_rango(vertice):
            return sum(self._matriz_ady[vertice, :])
    
    def incidencia(self, vertice):
         
        if self._dirigido:
            return self.grado_entrada(vertice) - self.grado_salida(vertice)
        else:
            return self.grado_entrada(vertice) + self.grado_salida(vertice)

    def recorrido_en_profundidad(self):
        visitados = [False*self._size]
        for i in range(self._size):
            if not visitados[i]:
                self.recorrer_en_profundidad(i, visitados)

    def recorrer_en_profundidad(self, v, visitados):
        visitados[v] = True

        for i in range(self._size):
            if self.existe_arista(v, i) and not visitados[i]:
                self.recorrer_en_profundidad(i, visitados)


    #TODO implementar recorrido en amplitud


    def es_grafo_conexo(self):
        visitados = [False*self._size]
        
        if self.get_dirigido():
            self.recorrerProfundidadCadena(0, visitados)
        else:
            self.recorrer_en_profundidad(0, visitados)

        return self.todosVisitados(visitados)

    
    def recorrerProfundidadCadena(self, v, visitados):
        visitados[v] = 1

        for i in range(self._size):
            if (self.existe_arista(v, i) or self.existe_arista(i, v)) and not visitados[i]:
                self.recorrerProfundidadCadena(self, i, visitados)
    
    def todosVisitados(self, visitados):
        result = True
        for v in visitados:
            if not v:
                result = False
                return result
        
        return result
    

    #TODO implementar metodo mostrar