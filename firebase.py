import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./burgerbot-f51db-firebase-adminsdk-52j29-acf6306076.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client(app)