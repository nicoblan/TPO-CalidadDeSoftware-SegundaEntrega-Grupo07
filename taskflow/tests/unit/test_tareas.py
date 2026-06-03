import pytest
from datetime import date, timedelta
from app.services.tareas import calcular_avance_proyecto, validar_fecha_limite

def test_avance_mitad_completadas():
    tareas = [
        {"estado": "completada"},
        {"estado": "en_progreso"},
        {"estado": "pendiente"},
        {"estado": "completada"}
    ]
    assert calcular_avance_proyecto(tareas) == 50.0

def test_avance_todas_completadas():
    tareas = [
        {"estado": "completada"},
        {"estado": "completada"},
        {"estado": "completada"}
    ]
    assert calcular_avance_proyecto(tareas) == 100.0

def test_avance_lista_vacia():
    assert calcular_avance_proyecto([]) == 0.0

def test_fecha_limite_valida():
    fecha_futura = date.today() + timedelta(days=7)
    assert validar_fecha_limite(fecha_futura) == True

def test_fecha_limite_pasada():
    fecha_pasada = date.today() - timedelta(days=1)
    with pytest.raises(ValueError):
        validar_fecha_limite(fecha_pasada)
