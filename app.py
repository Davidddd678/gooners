from flask import Flask,render_template
import random 

app = Flask(__name__)


@app.route('/')
def index():
    curiosidade_selecionada= ["eu gosto de goon", " eu tenho 15 anos", " eu adoro pessoas gulosas"]
    
    curiosidade = random.choice(curiosidade_selecionada)

    return render_template("index.html", visitas= 1, curiosidade=curiosidade )

app.run(host="0.0.0.0", port=8080, debug=True)
