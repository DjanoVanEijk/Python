import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = base_url + "pokemon/" + name
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Name: " + data["name"])
        print("Height: " + str(data["height"]))
        print("Weight: " + str(data["weight"]))
    else:
        print("Error: " + str(response.status_code))

pokemon_name = "pikachu"
get_pokemon(pokemon_name)