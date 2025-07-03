from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hOLA DESDE MI RAMA DE EXAMEN fINAL INF-650'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
