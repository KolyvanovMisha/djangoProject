from pymongo import MongoClient


def get_db_handle(djangoProject, host, port, username, password):
    client = MongoClient(host='mongodb0.example.com',
                         port=21017,
                         username='m.kolyvanov@radugamarket.shop',
                         password=1234
                         )
    db_handle = client[djangoProject]
    return db_handle, client


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
