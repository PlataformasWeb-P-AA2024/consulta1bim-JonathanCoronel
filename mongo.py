from pymongo import MongoClient
import csv

#Crear cliente para la conexion a la Mongo DB
client = MongoClient('localhost',27017)
dbase = client['torneo_tenis']
collection = dbase['partidos']

# acceder al archivo y extraer la informacion.
archivo = open('atp_tennis.csv', "r")

# Leer el archivo CSV
reader = csv.DictReader(archivo)

# Convertir cada fila del archivo en un diccionario
datos = []
for linea in reader:
    # Crear un nuevo diccionario con espacios eliminados para las claves y valores
    clean_linea = {key.strip(): value.strip() for key, value in linea.items()}
    datos.append(clean_linea)

# Cerrar el archivo
archivo.close()

# Insertar los diccionarios en la colección de MongoDB
if datos:
    collection.insert_many(datos)

#Listar los documentos
doc = collection.find()
for d in doc:
    print(d)




