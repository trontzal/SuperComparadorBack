from flask import Flask, jsonify
import requests
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route("/")
def bienvenidos():
    return "Proyecto de supermercados"

@app.route('/categorias/mercadona')
def get_mercadona_categorias():
    url = 'https://tienda.mercadona.es/api/categories/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Error en la solicitud'}), 500

@app.route('/productosEnCategoria/mercadona/<int:id>')
def get_mercadona_productos_en_categoria(id):
    url = f'https://tienda.mercadona.es/api/categories/{id}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Error en la solicitud'}), 500