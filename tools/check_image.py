"""检查图片链接，打印无效链接

"""

import requests
from pymongo import MongoClient
collection = MongoClient().bastogne.movie

movie = collection.find()

with open('image.txt', 'ab') as f:
    for mv in movie:
        try:
            r = requests.get(mv['image'])
            if r.status_code != 200:
                f.write((mv['image'] + '\n').encode())
            else:
                print(mv['id'])
        except Exception as e:
            continue


