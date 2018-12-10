from pymongo import MongoClient

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://127.0.0.1:27017')

# db 접속(attribute, dictionary, method)
db = client.mymongodb
#db = client['mymongo']
# db = client.get_database('mymongo')

# 새로운 collection 생성
collection = db.person
# collection = db['people']
# collection = db.get_collection('people')

# insert document (insert_one(), insert_many())
post = {'author': 'Mike', 'content': 'My first blog post!', 'tag': ['mymongodb', 'python', 'pymongo']}
collection.insert_one(post)

post = {'author': 'John', 'content': 'My first blog post!', 'tag': ['mymongodb', 'python', 'pymongo']}
post_id = collection.insert_one(post).inserted_id


collection.insert_many([{'number' : i} for i in range(10)])
print('document 갯수: ', collection.estimated_document_count())

data = list()
data.append({'name': 'acorn', 'age': 20})
data.append({'name': 'tom', 'age': 20})
data.append({'name': 'jerry', 'age': 20})

collection.insert_many(data)

for result in collection.find():
    print(result)

# document 조회 : find_one(), find()
print(collection.find_one({'author': 'John'}))

# document 수정(update_one(), update_many())
collection.update_one({'author': 'Mike'}, {'$set': {'content': 'My second blog post!'}})
print(collection.find_one({'author': 'Mike'}))