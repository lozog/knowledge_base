from mongoengine import connect

mongo_client = connect(host="mongodb://127.0.0.1:27017/knowledge_base")
db = mongo_client.knowledge_base