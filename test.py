import time
import pprint
import random
import string
from pymongo import MongoClient
import datetime


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return(rand_string)


client = MongoClient()
# print(client.get_database)
db = client.RadugaMarket
# print(db)
collection = db.users
# print(collection)

start = time.time()
users = db.users
user_count = 10 ** 6
for i in range(user_count):
    user = {
        "author": generate_random_string(8),
        "email": 'mail' + str(i) + '@mail.ru',
        "date": datetime.datetime.utcnow(),
        "adress": {
            'city': generate_random_string(8),
            'street': generate_random_string(8),
        }
    }
    users.insert_one(user)

print('Время для заполнения {} пользователей: {:.2f} секунд'.format(user_count, time.time() - start))

start = time.time()
# pprint.pprint(users.find_one({"email": "mail999999@mail.ru"}))
pprint.pprint(users.find_one({"author": ""
                                        "bsjxdaws"}))
print('Время для чтения {} пользователей: {:.2f} секунд'.format(user_count, time.time() - start))

# users.delete_many({"author": "Mike"})
