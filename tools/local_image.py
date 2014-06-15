"""修改图片链接地址

"""

from base64 import urlsafe_b64encode
from pymongo import MongoClient


client = MongoClient()
db = client.bastogne
collection = db.movie
movie = collection.find()


def change_image(old_url):
    return 'http://saveimage-douban.stor.sinaapp.com/image/' + urlsafe_b64encode(old_url.encode()).decode() + '.jpg'

for mv in movie:
    collection.update({'id': mv['id']}, {'$set': {'image': change_image(mv['image'])}})
