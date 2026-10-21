from flask import Flask,jsonify,request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
palavras=[

   {
       "id":1,
       "palavras": "goon",
       "nome": "le David"
   },
   {
        "id":2,
        "palavras": "le verity",
        "nome": "le David"
   },
   {
        "id":3,
        "palavras": "Gambare",
        "nome": "le David"
   },
]


@app.route('/')
def index():
    return 'Hello my little friends'

@app.route('/palavras')
def piada():
    return random.choice(palavras)

@app.route('/palavras/<int:id>')
def piada_id(id):
    if id < 1 or id > len(palavras):
        return'Essa piada não existe good lad, miaw,',404
    return piadas[id-1]
app.run(host="0.0.0.0", port=8080)