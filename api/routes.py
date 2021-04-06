from bson import ObjectId, DBRef
import calendar
from collections.abc import ValuesView
from datetime import datetime
from flask import Blueprint, Flask, request
from flask.json import JSONEncoder
import flask_wrappers as wrappers
import json
from mongoengine.queryset import QuerySet
from pprint import pprint
from pymongo.cursor import Cursor
from uuid import UUID

from db import db
from documents import Document

blueprint = Blueprint("documents", __name__)

class KBEncoder(JSONEncoder):
    """A JSON encoder that handles MongoDB types and other stuff"""

    def default(self, obj):
        if isinstance(obj, (ObjectId, DBRef)):
            return str(obj)
        if isinstance(obj, datetime):
            return float(calendar.timegm(obj.utctimetuple()))
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, (set, ValuesView)):  # ValuesView is e.g. dict_values
            return list(obj)
        if isinstance(obj, (Cursor, QuerySet)):
            return list(obj)
        return JSONEncoder.default(self, obj)


def respond(code: int = 200, **kwargs):
    return (
        json.dumps(dict(**kwargs), cls=KBEncoder),
        code,
        {"Content-type": "application/json; charset=utf-8"},
    )


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
