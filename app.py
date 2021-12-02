from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://app:1HGbaYcRmUr3Rgoq@cluster0.yph9l.mongodb.net/Termoduino?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def hello_world():
  return "<h1>Aplicacion corriendo en puerto 5000</h1>"

@app.route("/get_temp")
def get_temp():
  temperaturas = mongo.db.Temperaturas.find()
  for x in temperaturas:
    print(x)
  return temperaturas

@app.route("/save_temp/<temp>")
def save_temp(temp):
  if float(temp) < 10:
    return f"<h1>{temp} grados es mucho Frio</h1>"
  elif float(temp) < 20:
    return f"<h1>Fresco</h1>"
  elif float(temp) < 30:
    return f"<h1>Agradable</h1>"
  else:
    return f"<h1>Caluroso</h1>"
