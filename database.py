import json
import hashlib
def add_anime(anime_name, is_episode):
    anime_id = hashlib.sha256(anime_name.encode('utf-8')).hexdigest()[:16]
    episode_number = int(input("Ingrese el número del último episodio: "))
    anime_sinopsis = input("Ingrese la sinopsis del anime: ")
    anime_type = input("Ingrese el tipo de anime: ")
    anime_state = input("Ingrese el estado del anime: ")
    anime_categories = input("Ingrese las categorías del anime: ")

    try:
        with open('database.json', 'r') as file: data = json.load(file)
            
        data["animes"][anime_id] = {
            "id": anime_id,
            "name": anime_name,
            "type": anime_type,
            "sinopsis": anime_sinopsis,
            "episodes": episode_number,
            "state": anime_state,
            "categories": anime_categories,
            "episodeUrls": [[""] for _ in range(episode_number)]
        }

        if len(data['lastAnimes']) == 24: data['lastAnimes'].pop(0)
        data['lastAnimes'].append({"id": anime_id})

        if anime_type == "Film":
            if len(data['lastFilms']) == 24: data['lastFilms'].pop(0)
            data['lastFilms'].append({"id": anime_id})

        if anime_state == "Finalizado":
            if len(data['finishedAnimes']) == 24: data['finishedAnimes'].pop(0)
            data['finishedAnimes'].append({"id": anime_id})

        with open('database.json', 'w') as file: json.dump(data, file, indent=4)

        print("El anime se ha agregado correctamente.")
        if is_episode:
            add_episode(anime_name)
        else:
            main()

    except FileNotFoundError: print("Error: Archivo 'database.json' no encontrado. Asegúrate de tener el archivo de datos antes de ejecutar este script.")
    except json.JSONDecodeError: print("Error: No se pudo decodificar el archivo JSON. Asegúrate de que el archivo 'database.json' sea un JSON válido.")
    except ValueError: print("Error: Ingresa un número válido para el episodio.")
    except Exception as e: print(f"Error inesperado: {e}")

def add_episode(anime_name):
    anime_id = hashlib.sha256(anime_name.encode('utf-8')).hexdigest()[:16]
    episode_number = int(input("Ingrese el número del episodio: "))
    other_url = True
    urls = []

    while other_url:
        url = input("Ingrese la url del episodio: ")
        more_url = input("¿Desea añadir mas urls? (S/N): ")
        urls.append(url)
        if more_url != "S":
            other_url = False

    try:
        with open('database.json', 'r') as file: data = json.load(file)
        if len(data['lastEpisodes']) == 24: data['lastEpisodes'].pop(0)
        data['lastEpisodes'].append({"id": anime_id, "number": episode_number})
        data['animes'][anime_id]["episodeUrls"][episode_number-1] = urls
        with open('database.json', 'w') as file: json.dump(data, file, indent=4)

        print("Se ha agregado el episodio correctamente.")
        main()

    except FileNotFoundError: print("Error: Archivo 'database.json' no encontrado. Asegúrate de tener el archivo de datos antes de ejecutar este script.")
    except json.JSONDecodeError: print("Error: No se pudo decodificar el archivo JSON. Asegúrate de que el archivo 'database.json' sea un JSON válido.")
    except ValueError: print("Error: Ingresa un número válido para el episodio.")
    except Exception as e: print(f"Error inesperado: {e}")

def main():
    command = input("/")
    if command.split(" ")[0] == "add":
        if command.split(" ")[1] == "episode":
            if len(command.split(" ")) >= 3:
                anime_name = command.replace("add episode ","")
                anime_id = hashlib.sha256(anime_name.encode('utf-8')).hexdigest()[:16]
                with open('database.json', 'r') as file: data = json.load(file)
                if anime_id not in data["animes"]:
                    add_anime(anime_name, True)
                else:
                    add_episode(anime_name)
            else:
                print("")
        if command.split(" ")[1] == "anime":
            if len(command.split(" ")) >= 3:
                anime_name = command.replace("add anime ","")
                anime_id = hashlib.sha256(anime_name.encode('utf-8')).hexdigest()[:16]
                with open('database.json', 'r') as file: data = json.load(file)
                if anime_id not in data["animes"]:
                    add_anime(anime_name, True)
                else:
                    print("")
            else:
                print("")
    main()
if __name__ == "__main__":
    main()
