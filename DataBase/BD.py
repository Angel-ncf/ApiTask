#conectar mongo db a main.py de Mini_Api_Proyecto
from pymongo import MongoClient

db_connection = MongoClient("mongodb://localhost:27017/")