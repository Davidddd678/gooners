from flask import Flask,render_template
from gpiozero import LED
import random 

led = LED(27)
app = Flask(__name__)

visitas = 0

@app.route('/')
def index():
    global visitas
    visitas = visitas +1
    curiosidade_selecionada= ["eu gosto de goon", " eu tenho 15 anos", " eu adoro pessoas gulosas"]
    
    curiosidade = random.choice(curiosidade_selecionada)

    return render_template("index.html",
                           led_status=led.is_lit,
                           curiosidade=curiosidade )

@app.route('/led/<string:status>')
def led_page(status):

    global led

    if status == "ON":
        led.on()
        return "GOON!"
    if status == "OFF":
        led.off()
        return "GOOFF"
    else:
        return" ERROR", 404


app.run(host="0.0.0.0", port=8080, debug=True, use_reloder=False)