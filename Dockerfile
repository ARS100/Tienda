# Imagen base de Python
FROM python:3.10

# Crear directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias primero (para cache de Docker)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer el puerto 8000 (Django por defecto)
EXPOSE 8000

# Comando para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]