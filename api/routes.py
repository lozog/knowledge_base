from flask import Blueprint, Flask, request
import flask_wrappers as wrappers

from documents import Document

blueprint = Blueprint("documents", __name__)

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
