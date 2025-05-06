# Utilizar el siguiente comando para ejecutar las pruebas en la terminal:
# python -m pytest ejercicio.py -v

import pytest
from amigos_etsisi import AmigosETSISI
from persona import Persona

@pytest.fixture
def setup_red_amistades():
    # Inicializamos la red de amistades con los contactos
    contactos = [
        Persona("Juan", 123456, "Gaztambide"),
        Persona("Jose", 231465, "Princesa"),
        Persona("Eva", 321654, "Gran Vía"),
        Persona("Alicia", 789456, "Castellana"),
        Persona("Alan", 654321, "Arboleda"),
        Persona("Guillermo", 159267, "Alcalá"),
        Persona("Julio", 354326, "Gaztambide"),
        Persona("Lucas", 753842, "Serrano"),
        Persona("Paula", 367834, "Velazquez"),
        Persona("Clara", 875225, "Castellana"),
    ]
    
    # Creamos la red de amistades
    red = AmigosETSISI(len(contactos), contactos)

    # Creamos las relaciones de amistad (aristas) entre los contactos
    relaciones = [
        (5, 4), (5, 6), (4, 6),        # Grupo 1: Guillermo, Alan, Julio
        (8, 3), (3, 2), (3, 0),        # Grupo 2: Paula, Alicia, Eva, Juan
        (2, 1), (0, 1),                # Conexiones extra dentro del grupo 2
        (7, 9)                         # Grupo 3: Lucas, Clara
    ]
    
    # Insertamos las relaciones en la red
    for a, b in relaciones:
        red.inserta_relacion(a, b)

    return red

def test_contar_grupos(setup_red_amistades):
    assert setup_red_amistades.contar_grupos() == 3

def test_mostrar_amigos_existente(setup_red_amistades):
    resultado = setup_red_amistades.mostrar_amigos("Guillermo")
    assert "Alan" in resultado and "Julio" in resultado

def test_mostrar_amigos_no_existente(setup_red_amistades):
    assert setup_red_amistades.mostrar_amigos("Inexistente") == "No se encontró a Inexistente en la red."

def test_son_del_mismo_grupo_true(setup_red_amistades):
    assert setup_red_amistades.son_del_mismo_grupo("Guillermo", "Julio") is True
    assert setup_red_amistades.son_del_mismo_grupo("Alicia", "Jose") is True

def test_son_del_mismo_grupo_false(setup_red_amistades):
    assert setup_red_amistades.son_del_mismo_grupo("Guillermo", "Lucas") is False

def test_son_del_mismo_grupo_mismos_nombres(setup_red_amistades):
    assert setup_red_amistades.son_del_mismo_grupo("Paula", "Paula") is True

def test_son_del_mismo_grupo_persona_no_existente(setup_red_amistades):
    with pytest.raises(ValueError):
        setup_red_amistades.son_del_mismo_grupo("Guillermo", "Desconocido")

def test_mostrar_miembros_grupo_existente(setup_red_amistades):
    resultado = setup_red_amistades.mostrar_miembros_grupo("Paula")
    assert all(nombre in resultado for nombre in ["Paula", "Alicia", "Eva", "Juan", "Jose"])

def test_mostrar_miembros_grupo_no_existente(setup_red_amistades):
    assert setup_red_amistades.mostrar_miembros_grupo("Inexistente") == "La persona 'Inexistente' no existe en la red."

def test_mostrar_saltos_amistad_existente(setup_red_amistades):
    resultado = setup_red_amistades.mostrar_saltos_amistad("Paula")
    assert "- Alicia: 1 salto(s)" in resultado
    assert "- Eva: 2 salto(s)" in resultado
    assert "- Juan: 2 salto(s)" in resultado
    assert "- Jose: 3 salto(s)" in resultado

def test_mostrar_saltos_amistad_no_existente(setup_red_amistades):
    assert setup_red_amistades.mostrar_saltos_amistad("Inexistente") == "No se encontró a Inexistente en la red."
