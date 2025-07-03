
import requests
import json

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic",
        auth=authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")


def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={
            "Content-type": "application/json",
            "X-API-Key": apiKey
        },
        data=json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Libro agregado: {book}")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, al intentar agregar el libro {book}.")

apiKey = getAuthToken()

book = {
    "id": 20,
    "title": "Examen Final Programacion Redes",
    "author": "JosueAbelFloresCruz"
}

addBook(book, apiKey)
