import mongoengine
from mongoengine import StringField, ObjectIdField, ListField

class Document(mongoengine.Document):
    title = StringField(max_length=200, required=True)
    content = StringField(max_length=10240, required=True)
    parent = ObjectIdField()
    children = ListField(ObjectIdField())
    meta = {'collection': 'documents'}
