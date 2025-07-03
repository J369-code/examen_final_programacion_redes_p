import json

with open('usuarios.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

for persona in datos:
    print(persona['nombre'])
