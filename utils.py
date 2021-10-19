from pymongo import MongoClient


def get_db_handle(djangoProject2, host, port, username, password):
    client = MongoClient(host='localhost',
                         port=21017,
                         username='',
                         password=''
                         )
    db_handle = client[djangoProject2]
    return db_handle, client


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
