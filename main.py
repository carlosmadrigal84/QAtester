import requests
import json

def obtener_informacion_personaje(nombre_personaje):
    # URL de la API de Rick and Morty para buscar el personaje por nombre
    url_personaje = f'https://rickandmortyapi.com/api/character/?name={nombre_personaje}'

    # Realizar la solicitud para obtener información del personaje
    response_personaje = requests.get(url_personaje)

    # Verificar si la solicitud fue exitosa
    if response_personaje.status_code == 200:
        personajes = response_personaje.json()["results"]

        # Verificar si se encontraron personajes con el nombre dado
        if personajes:
            personaje = personajes[0]

            # Obtener información del personaje
            info_personaje = {
                "especie": personaje["species"],
                "tipo": personaje["type"],
                "longitud_nombre": len(personaje["name"])
            }

            # Obtener información de la ubicación
            ubicacion_url = personaje["location"]["url"]
            response_ubicacion = requests.get(ubicacion_url)
            ubicacion = response_ubicacion.json()
            info_ubicacion = {
                "nombre": ubicacion["name"],
                "tipo": ubicacion["type"],
                "dimension": ubicacion["dimension"],
                "poblacion": ubicacion["residents"]
            }

            # Obtener información de los episodios
            episodios = personaje["episode"]
            info_episodios = []
            for episodio_url in episodios:
                response_episodio = requests.get(episodio_url)
                episodio = response_episodio.json()
                info_episodios.append({
                    "nombre_episodio": episodio["name"],
                    "id_episodio": episodio["id"],
                    "cantidad_personajes": len(episodio["characters"])
                })

            # Crear la respuesta con la información
            respuesta = {
                "Información del personaje": info_personaje,
                "Información de la ubicación": info_ubicacion,
                "Información de los episodios": info_episodios
            }

            return respuesta

        else:
            return "No se encontró un personaje con ese nombre."

    else:
        return "Error al obtener información del personaje."

# Probando código
personaje_buscar = "Reverse Giraffe"
informacion_personaje = obtener_informacion_personaje(personaje_buscar)
print("<<< La respuesta debe contener la siguiente información:")
print("Información del personaje ->", informacion_personaje["Información del personaje"])
print("Información de la ubicación ->", informacion_personaje["Información de la ubicación"])
print("Información de los episodios ->", informacion_personaje["Información de los episodios"])

