from pymongo import MongoClient


client = MongoClient()
db = client.bastogne
collection = db.movie


def get_genres():
    genres = collection.distinct('genres')
    data = []

    for genre in genres:
        data.append({'tag': genre, 'count': collection.find({'genres': genre}).count()})

    return data


if __name__ == '__main__':
    print(get_genres())