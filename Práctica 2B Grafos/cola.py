class NodoCola:
    def __init__(self, valor):
        """Inicializa un nodo con un valor y un puntero al siguiente nodo."""
        self.__valor = valor
        self.__siguiente = None

    def get_valor(self):
        """Devuelve el valor del nodo."""
        return self.__valor

    def set_valor(self, valor):
        """Establece el valor del nodo."""
        self.__valor = valor

    def get_siguiente(self):
        """Devuelve el siguiente nodo."""
        return self.__siguiente

    def set_siguiente(self, siguiente):
        """Establece el siguiente nodo."""
        self.__siguiente = siguiente


class Cola:
    def __init__(self):
        """Inicializa una cola vacía."""
        self.__longitud = 0
        self.__primero = None
        self.__ultimo = None

    def longitud(self):
        """Devuelve la longitud de la cola."""
        return self.__longitud

    def vacia(self):
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return self.__longitud == 0

    def encolar(self, elem):
        """
        Agrega un elemento al final de la cola.

        Args:
            elem: El elemento a agregar.
        """
        nodo = NodoCola(elem)  # Creamos el nuevo nodo con el elemento dado
        if not self.vacia():  # Si la cola no está vacía
            self.__ultimo.set_siguiente(nodo)  # Enlazamos el último nodo con el nuevo
        else:
            self.__primero = nodo  # Si está vacía, el primero apunta al nuevo nodo
        self.__ultimo = nodo  # Actualizamos el último nodo al nuevo nodo
        self.__longitud += 1  # Incrementamos el tamaño de la cola

    def desencolar(self):
        """
        Elimina y devuelve el primer elemento de la cola.

        Returns:
            El valor del elemento eliminado, o None si la cola está vacía.
        """
        elemento = None
        if not self.vacia():  # Si la cola no está vacía
            elemento = self.__primero.get_valor()  # Obtenemos el valor del primer nodo
            self.__primero = self.__primero.get_siguiente()  # Actualizamos el primero al siguiente nodo
            self.__longitud -= 1  # Decrementamos el tamaño de la cola
            if self.vacia():  # Si la cola queda vacía
                self.__ultimo = None  # El último nodo apunta a None
        return elemento
