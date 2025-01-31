# Usar la imagen oficial de Python
FROM python:3.8

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar dependencias necesarias
RUN pip install flask

# Exponer el puerto 7529
EXPOSE 7529

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
