from flask import Flask, send_from_directory,jsonify,request
from conexion import select

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/mysql')
def prueba():
    datos=select("select * from usuarios")
    return jsonify(datos)

@app.route('/calcular', methods=['POST'])
def ajax():
    data = request.get_json()
    ancho = float(data['ancho'])/1000
    alto = float(data['alto'])/1000
    tipo = data['tipo']
    precio=0;
    if(tipo=="blanco.jpg"):
        precio=3*ancho*alto;
    elif (tipo=="madera.jpg"):
        precio=5*ancho*alto;
    else:
        precio=10*ancho*alto;
  
    # Hacer algo con los parámetros recibidos
    return jsonify({
        'ancho':ancho,
        'alto':alto,
        'tipo':tipo,
        'precio':precio
    })

if __name__ == '__main__':
    app.run()

