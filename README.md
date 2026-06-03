# 📋 TaskFlow - Gestión de Tareas

### Trabajo Práctico Obligatorio - Calidad de Software

TaskFlow es una aplicación base desarrollada con **FastAPI** cuyo objetivo es demostrar la aplicación de buenas prácticas de desarrollo de software, incluyendo pruebas automatizadas, análisis de calidad de código y un pipeline de Integración Continua (CI).

---

## 🚀 Características

* ✅ **Lógica de negocio:** funciones para calcular el progreso de proyectos y validar fechas límite.
* ✅ **Calidad de código:** configuración de `flake8` para análisis estático y cumplimiento de estándares de desarrollo.
* ✅ **Testing:** pruebas unitarias implementadas con `pytest` y generación de reportes de cobertura.
* ✅ **CI/CD:** pipeline automatizado mediante GitHub Actions para validación continua del proyecto.

---

## 🛠️ Estructura del Proyecto

```text
taskflow/
├── .github/
│   └── workflows/          # Configuración de GitHub Actions (CI)
├── app/
│   ├── services/           # Lógica de negocio (tareas.py)
│   └── __init__.py
├── tests/
│   ├── unit/               # Pruebas unitarias (test_tareas.py)
│   └── __init__.py
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación
```

---

## 💻 Instalación Local

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd taskflow
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```

**Activar entorno virtual en Windows:**

```bash
.\venv\Scripts\activate
```

**Activar entorno virtual en Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecución de Pruebas

Para ejecutar las pruebas unitarias y generar el reporte de cobertura:

```bash
pytest tests/unit/ -v --cov=app
```

---

## ⚙️ Pipeline de Integración Continua (CI)

El proyecto incorpora un flujo de trabajo automatizado mediante **GitHub Actions**, que se ejecuta automáticamente ante cada:

* `push`
* `pull_request`

sobre las ramas:

* `main`
* `develop`

### El pipeline realiza las siguientes validaciones:

1. Instalación automática de dependencias.
2. Análisis de calidad y estilo de código con `flake8`.
3. Ejecución de pruebas unitarias mediante `pytest`.
4. Verificación de una cobertura mínima del **70%**.

---

## 📌 Tecnologías Utilizadas

* Python
* FastAPI
* Pytest
* Flake8
* GitHub Actions

---

## 👥 Equipo

Proyecto desarrollado para la materia **Calidad de Software** como parte de la segunda etapa del TPO.
