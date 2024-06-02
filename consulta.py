from pymongo import MongoClient

#Crear cliente para la conexion a la Mongo DB
client = MongoClient('localhost',27017)
dbase = client['torneo_tenis']
collection = dbase['partidos']


# Función para encontrar todos los partidos en los que participo un jugador.
def encontrar_jugador(nombre_jugador):
    consulta = {
        "$or": [
            {"Player_1": nombre_jugador},
            {"Player_2": nombre_jugador}
        ]
    }

    # Proyección para incluir solo ciertos campos
    proyeccion = {
        "_id": 0,
        "Tournament": 1,
        "Date": 1,
        "Player_1": 1,
        "Player_2": 1,
        "Winner": 1,
        "score": 1
    }

    partidos = collection.find(consulta,proyeccion)
    return list(partidos)

#Nombre del jugador a buscar
nombre_jugador = "Reister J."

# Obtener y mostrar los partidos en los que participó el jugador
partidos_jugador = encontrar_jugador(nombre_jugador)
print(f"Todos los partidos en los que participo {nombre_jugador}:")
for s in partidos_jugador:
    print(s)