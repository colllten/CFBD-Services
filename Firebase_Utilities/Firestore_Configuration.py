import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
def configure_firestore():
    cred = credentials.Certificate("b1g-fantasy-football-firebase-adminsdk-yg8ju-e1df3c0765.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
