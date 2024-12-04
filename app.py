import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Credenciales de la API de Imagga
API_KEY = 'acc_5c2fe763caeb831'
API_SECRET = '1f3d16f24adc9947c9cfc33e814dd128'
API_URL = 'https://api.imagga.com/v2/tags'

# Lista de URLs de imágenes (nuevas imágenes)
images = [
    "https://upload.wikimedia.org/wikipedia/commons/8/89/Tiger_in_Ranthambhore.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/e8/Sunflower_from_Silesia2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/cd/Blue_butterfly_at_the_Museum_of_Life_and_Science.JPG"
]

@app.route('/')
def index():
    return render_template('index.html', images=images)

@app.route('/analyze', methods=['POST'])
def analyze():
    results = []

    # Procesar cada imagen seleccionada
    for image_url in request.form.getlist('images'):
        # Solicitar etiquetas al API de Imagga
        response = requests.get(API_URL, auth=(API_KEY, API_SECRET), params={'image_url': image_url})
        data = response.json()

        # Validar que la respuesta contenga etiquetas
        if 'result' in data and 'tags' in data['result']:
            tags = data['result']['tags']

            # Ordenar las etiquetas por confianza y tomar las dos más confiables
            sorted_tags = sorted(tags, key=lambda x: x['confidence'], reverse=True)
            top_tags = sorted_tags[:2]

            # Agregar los resultados a la lista
            results.append({
                'image': image_url,
                'tags': [{'tag': tag['tag']['en'], 'confidence': round(tag['confidence'], 2)} for tag in top_tags]
            })
        else:
            # Manejar errores o respuestas sin etiquetas
            results.append({
                'image': image_url,
                'tags': [{'tag': 'No tags found', 'confidence': 0}]
            })

    # Renderizar los resultados en la plantilla
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
