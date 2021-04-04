from flask import Flask, request
import flask_wrappers as wrappers
from mongoengine import connect

from documents import Document

app = Flask(__name__)

connect(host="mongodb://127.0.0.1:27017/knowledge_base")


@app.route('/documents', methods=["POST"])
@wrappers.json_request
def create_document(body):
    try:
        title = body["title"]
        content = body["content"]
        parent = body.get("parent")
        children = body.get("children")
    except KeyError:
        return "Data missing from request"

    document = Document(**{
        "title": title,
        "content": content,
        "parent": parent,
        "children": children
    })
    document.save()

    return f"Inserted as {document.id}"