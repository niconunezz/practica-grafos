class Persona:
    def __init__(self, nombre: str, telefono: str, direccion: str):
        self._nombre = nombre
        self._telefono = telefono
        self._direccion = direccion

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_telefono(self):
        return self._telefono
    
    def set_telefono(self, telefono):
        self._telefono = telefono
    
    def get_direccion(self):
        return self._direccion
    
    def set_direccion(self, direccion):
        self._direccion = direccion

    def mostrar_persona(self):
        return f"{self.get_nombre()} ({self.get_telefono()}) {self.get_direccion()}"
