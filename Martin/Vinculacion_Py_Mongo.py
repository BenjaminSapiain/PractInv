from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI) # Conexion a base de datos.

db = client["infraestructura"]  # Nombre de base de datos.

collection = db["organismo"]    # Nombre de la coleccion.