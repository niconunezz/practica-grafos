from grafo import GrafoMA
from persona import Persona

# ============================================================================ #
# Realizado por: Javier De Jesus y Nicolás Nuñez
# ============================================================================ #


class AmigosETSISI:
    def __init__(self, n, contactos):
        """
        Inicializa una red de amistades con n personas y su información de contacto.
        
        Args:
            n: Número de personas en la red
            contactos: Lista de objetos Persona que representan los contactos
        """
        self.__red = GrafoMA(n, dirigido=False)
        self.__contactos = contactos
        self.__contacto_a_pos = {
            contacto.get_nombre().lower(): i
            for i, contacto in enumerate(contactos)
        }

    def get_num_personas(self):
        """Devuelve el número de personas en la red."""
        return self.__red.get_num_vertices()

    # ============================================================================ #
    # MÉTODOS PARA GESTIONAR RELACIONES (ARISTAS)
    # ============================================================================ #

    def inserta_relacion(self, o, d):
        """
        Inserta una relación de amistad directa (una arista en el grafo).
        
        Args:
            o: Vértice de origen
            d: Vértice de destino
        """
        self.__red.insertar_arista(o, d)

    def elimina_relacion(self, o, d):
        """
        Elimina una relación de amistad directa (una arista en el grafo).
        
        Args:
            o: Vértice de origen
            d: Vértice de destino
        """
        self.__red.elimina_arista(o, d)

    def existe_relacion(self, o, d):
        """
        Comprueba si existe una relación de amistad directa (una arista en el grafo).
        
        Args:
            o: Vértice de origen
            d: Vértice de destino
            
        Returns:
            Booleano que indica si la relación existe
        """
        return self.__red.existe_arista(o, d)

    def devuelve_pos_nombre(self, nombre):
        """
        Encuentra la posición asociada con el nombre de una persona en la tabla de contactos.
        
        Args:
            nombre: Nombre a buscar
            
        Returns:
            Posición del índice del nombre, o -1 si no se encuentra
        """
        return self.__contacto_a_pos.get(nombre.lower(), -1)

    def imprime_relaciones(self):
        """Imprime la matriz de relaciones en la consola."""
        print("Contenido de la matriz")
        print("  ", end=" ")
        for i in range(self.get_num_personas()):
            if i < 10:
                print(" " + str(i) + " ", end=" ")
            else:
                print(str(i) + " ", end=" ")
        print()
        for i in range(self.get_num_personas()):
            if i < 10:
                print(" " + str(i), end=" ")
            else:
                print(str(i), end=" ")
            for j in range(self.get_num_personas()):
                if self.existe_relacion(i, j):
                    print(" S ", end=" ")
                else:
                    print(" N ", end=" ")
            print()

    def mostrar_red(self):
        """Muestra información sobre la red y la matriz de relaciones."""
        print(f"Existen {self.get_num_personas()} contactos: ")
        for i, contacto in enumerate(self.__contactos):
            print(f"{i}: {contacto.get_nombre()}")
        self.imprime_relaciones()
        print()

    # ============================================================================ #
    # Métodos a completar
    # ============================================================================ #

    # Primer método a completar
    def contar_grupos(self) -> int:
        """
        Cuenta el número de grupos de amigos desconectados en la red.

        Returns:
            Número de grupos de amigos
        """
        
        # Inicializamos el conjunto de vértices visitados
        visitados = [False] * self.__red.get_num_vertices()
        grupos = 0

        for vertice, visitado in enumerate(visitados):
            if not visitado:
                # Realizamos un recorrido en profundidad para marcar todos los vértices en el grupo
                self.__red.recorrido_en_profundidad_desde_vertice(vertice, visitados, False)
                grupos += 1

        return grupos



    # Segundo método a completar
    def mostrar_amigos(self, nombre: str) -> str | None:
        """
        Muestra todos los amigos directos de una persona dada.
        
        Args:
            nombre: Nombre de la persona
        """
        
        # Obtenemos la posición del nombre en la red
        pos = self.devuelve_pos_nombre(nombre)
        if pos == -1:
            return f"No se encontró a {nombre} en la red."

        # Obtenemos la lista de amigos directos
        amigos = [
            self.__contactos[persona].get_nombre()
            for persona in range(self.get_num_personas())
            if self.existe_relacion(pos, persona)
        ]
                
        if not amigos:
            return f"{nombre} no tiene amigos directos en la red."
            
         # Formateamos y devolvemos la lista de amigos
        return (
            f"Amigos de {nombre}:\n" + 
            "\n".join(f"- {amigo}" for amigo in amigos)
        )



    # Tercer método a completar
    def son_del_mismo_grupo(self, persona1: str, persona2: str) -> bool:
        """
        Comprueba si dos personas pertenecen al mismo grupo de amigos.
        
        Args:
            persona1: Nombre de la primera persona
            persona2: Nombre de la segunda persona
            
        Returns:
            Booleano que indica si están en el mismo grupo
        """
        # Obtenemos las posiciones de las personas en la red
        # Si no se encuentran, lanzamos una excepción
        if (pos1 := self.devuelve_pos_nombre(persona1)) == -1:
            raise ValueError(f"Persona no encontrada: {persona1}")
        
        if (pos2 := self.devuelve_pos_nombre(persona2)) == -1:
            raise ValueError(f"Persona no encontrada: {persona2}")
        
        # Si ambas posiciones son iguales, pertenecen al mismo grupo
        if pos1 == pos2:
            return True
        
        # Realizamos un recorrido en profundidad desde la primera persona
        visitados = [False] * self.get_num_personas()
        self.__red.recorrido_en_profundidad_desde_vertice(pos1, visitados)
        
        # Si fue visitada, significa que pertenece al mismo grupo
        return visitados[pos2]

    # Cuarto método a completar
    def mostrar_miembros_grupo(self, persona: str) -> str | None:
        """
        Muestra todos los miembros del grupo de amigos que incluye a la persona dada.
        
        Args:
            persona: Nombre de la persona
        """
        
        # Obtenemos la posición de la persona en la red
        # Si no se encuentra, devolvemos un mensaje de error
        if (pos := self.devuelve_pos_nombre(persona)) == -1:
            return f"La persona '{persona}' no existe en la red."

        # Realizamos un recorrido en profundidad desde la persona dada
        # para obtener todos los miembros del grupo
        visitados = [False] * self.get_num_personas()
        self.__red.recorrido_en_profundidad_desde_vertice(pos, visitados)
        
        # Formateamos la salida
        miembros = [
            f"- {self.__contactos[i].mostrar_persona()}"
            for i, visitado in enumerate(visitados)
            if visitado
        ]
        
        return (
            f"Miembros del grupo de {persona}:\n" +
            "\n".join(miembros)
        )


    # (OPCIONAL) Quinto método a completar
    def mostrar_saltos_amistad(self, persona) -> str | None:
        """
        Dada una persona, muestra todos los miembros de su grupo de amigos y 
        cuántos saltos de amistad hay entre ellos.

        Args:
            persona: Nombre de la persona
        """
        
        # Obtenemos la posición de la persona en la red
        pos = self.devuelve_pos_nombre(persona)
        
        # Si no se encuentra, devolvemos un mensaje de error
        if pos == -1:
            return f"No se encontró a {persona} en la red."
        
        # Realizamos un recorrido en amplitud desde la persona dada
        # para obtener los saltos de amistad
        saltos = self.__red.recorrido_amplitud_desde_vertice(pos)

        # Formateamos la salida
        resultado = [f"Saltos de amistad desde {persona}:"]
        
        resultado.extend(
            f"- {self.__contactos[i].get_nombre()}: {saltos[i]} salto(s)"
            for i in range(self.get_num_personas())
            if saltos[i] != -1 and i != pos
        )

        return "\n".join(resultado)

