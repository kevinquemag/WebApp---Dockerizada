Para ejecutar el programa se necesta realizar los siguientes pasos

1.-Instalar las librerias de flask que estan en el archivo requirements.txt

Este proyecto es una aplicación web que utiliza Flask para analizar imágenes mediante el servicio SaaS de Imagga.

## Características
- Muestra una lista de imágenes desde URLs públicas.
- Analiza cada imagen utilizando la API de Imagga y muestra las dos etiquetas más confiables.

## Requisitos
- Docker instalado en la máquina.

2.-Contruimos la imagen

docker build -t image-analyzer .

3.-Ejecutamos la app dockerizada

docker run -p 5000:5000 image-analyzer

4.-Ejecutar app.py

python app.py

5.-Ingresamos al host

http://127.0.0.1:5000/
