from flask import Flask

from db import db

app = Flask(__name__)

@app.route('/documents', methods=["POST"])
def create_document():
    documents = db.documents
    document = {
        "title": "test document",
        "content": "lorem ipsum",
        "parent": None,
        "children": []
    }
    document_id = documents.insert_one(document).inserted_id
    return f"Inserted as {document_id}"