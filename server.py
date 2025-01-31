from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Servidor Flask funcionando en el puerto 7890!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7890, debug=True)
