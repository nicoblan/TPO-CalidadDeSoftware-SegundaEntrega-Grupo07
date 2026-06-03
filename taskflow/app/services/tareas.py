from datetime import date

def calcular_avance_proyecto(tareas: list) -> float:
    if not tareas:
        return 0.0
    completadas = sum(1 for t in tareas if t["estado"] == "completada")
    return round((completadas / len(tareas)) * 100, 1)

def validar_fecha_limite(fecha_limite: date) -> bool:
    if fecha_limite < date.today():
        raise ValueError("La fecha límite no puede ser anterior a hoy")
    return True
