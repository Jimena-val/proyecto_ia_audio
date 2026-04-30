Este proyecto permite analizar una pieza musical mediante Inteligencia Artificial para identificar los instrumentos presentes en una canción.

La aplicación utiliza:

- Python
- Flask
- TensorFlow
- TensorFlow Hub
- Librosa

---

# ⚠ Requisitos importantes antes de ejecutar ⚠

Debido a que este proyecto utiliza **TensorFlow**, es importante saber que **no es compatible con todas las versiones de Python**.

Actualmente se recomienda utilizar únicamente:

**Python 3.11.x**

Versiones más recientes como Python 3.12 o superiores pueden generar errores de compatibilidad.

así que...

# Paso 1: Instalar Python 3.11.x en Windows

Descargar Python desde el sitio oficial -> [https://www.python.org/downloads/windows/]

Durante la instalación es MUY IMPORTANTE activar la opción:

✔ **Add Python to PATH**

Esto permitirá ejecutar Python desde la terminal de VS Code.

---

# Paso 2: Reiniciar el equipo

Después de instalar Python:

Reiniciar Windows

Esto ayuda a que las variables del sistema se actualicen correctamente.

---

# ✅ Paso 3: Clonar el repositorio

Abrir VS Code y clonar el proyecto:

# Paso 4: Instalar dependencias
Desde la terminal de VS Code ejecutar:
pip install flask tensorflow tensorflow-hub librosa numpy soundfile
Esto instalará todas las librerías necesarias para el proyecto.

# Paso 5: Ejecutar el servidor
Una vez instaladas las dependencias ejecutar:
python app.py

Si todo es correcto aparecerá algo similar a: Running on http://127.0.0.1:5000

# Paso 6: Abrir en navegador

# NOTA -> Este proyecto usa un modelo preentrenado para clasificación de audio, por lo que algunos resultados pueden variar dependiendo de la calidad del archivo musical.
