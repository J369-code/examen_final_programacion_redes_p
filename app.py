from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '!hola desde mi aplicacion docker INF-651'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
