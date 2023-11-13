print("hola mundo")


import requests
import json
import time
import random

#response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=4&limit=1")
#print(response.json())

repeticiones = 0

while repeticiones < 3:
    offset = random.randint(1, 200)
    url = f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit=4"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        print(f'{pokemon["results"][0]["name"]}')
        print(f'{pokemon["results"][1]["name"]}')
        print(f'{pokemon["results"][2]["name"]}')
        print(f'{pokemon["results"][3]["name"]}')
    else:
        print(f"Error en la sulicitud.")
    
    repeticiones += 1    
    time.sleep(2)



#print(f'{pokemon["results"][0]["name"]}\n{pokemon["results"][1]["name"]}')
