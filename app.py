from flask import Flask
import random

app = Flask(__name__)

piadas=[" Porque é a galinha atravessou a estrada? Para chegar ao outro lado",
        " Qual é o animal mais velho do mundo, não sei? Nem eu ..."]

@app.route('/')
def index():
    return 'Hello my little friends'

@app.route('/piada')
def piada():
    return random.choice(piadas)

@app.route('/piada/<int:id>')
def piada_id(id):
    if id < 1 or id > len(piadas):
        return'Piada não encontrada?',404
    return piadas[id-1]
app.run(host="0.0.0.0", port=8080)