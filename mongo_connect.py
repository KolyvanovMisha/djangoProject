from pymongo import MongoClient


collections = {
    'USER': 'users',
    'POST': 'post',
}



def mongo_connection(coll_name):
    client = MongoClient()
    db = client.RadugaMarket
    collection_name = collections[coll_name]
    print('Вещаю из монго коннекта, иду в коллекцию: {}'.format(collection_name))
    # Не понимаю как в точечную нотацию подставить переменную,
    # которая лежит в collection_name
    collection = db.users
    return collection


