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
    res = db.documents.find_one({"_id": ObjectId(document_id)})

    return respond(document=res)


@blueprint.route('/documents', methods=["POST"])
def create_document():
    body = request.get_json()
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

    return respond(document=document.to_mongo())


@blueprint.route('/documents/<document_id>', methods=["PATCH"])
def update_document(document_id):
    body = request.get_json()
    updated_document_count = Document.objects.update_one(id=document_id, **{
        k: v
        for k, v in body.items()
        if k in ["title", "parent", "children", "content"]
    })

    return respond(updated_document_count=updated_document_count)
