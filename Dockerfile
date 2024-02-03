# Usa una imagen base de Python
FROM python:3.10.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Comando para ejecutar la aplicación (ajústalo según tu configuración)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
