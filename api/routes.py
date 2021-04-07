from bson import ObjectId
from flask import Blueprint, request

from db import db
from documents import Document
from helpers import respond

blueprint = Blueprint("documents", __name__)


@blueprint.route('/documents', methods=["GET"])
def get_documents():
    res = list(db.documents.find())

    return respond(documents=res)


@blueprint.route('/documents/<document_id>', methods=["GET"])
def get_document(document_id):
    res = list(db.documents.find({"_id": ObjectId(document_id)}))

    return respond(documents=res)


@blueprint.route('/documents', methods=["POST"])
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
