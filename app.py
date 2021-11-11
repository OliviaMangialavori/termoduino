from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<h1>Aplicacion corriendo en puerto 5000</h1>"

@app.route("/save_temp/<temp>")
def save_temp(temp):
  if float(temp) < 10:
    return f"<h1>Frio</h1>"
  elif float(temp) < 20:
    return f"<h1>Fresco</h1>"
  elif float(temp) < 30:
    return f"<h1>Agradable</h1>"
  else:
    return f"<h1>Caluroso</h1>"
