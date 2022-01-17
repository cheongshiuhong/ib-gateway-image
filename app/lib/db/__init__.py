from google.cloud import firestore

dbClient = firestore.Client()

class DbClient(firestore.Client):
    def __init__(self):
        super().__init__()
