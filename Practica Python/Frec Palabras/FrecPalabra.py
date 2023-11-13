print("Hola Mundo")

import requests
import json
import time

#response= requests.get("https://api.chucknorris.io/jokes/random")
#print(response.json())

while True :
    response = requests.get("https://api.chucknorris.io/jokes/random")
    chiste = response.json()
    with open(r"C:\Users\hugof\OneDrive\Escritorio\EDEM\Practica Python\Frec Palabras\test.txt", "a") as file:
        file.write(chiste["value"] + '\n')

    time.sleep(5)


    #print(chiste['value'])