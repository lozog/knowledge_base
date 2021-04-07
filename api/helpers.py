from bson import DBRef, ObjectId
import calendar
from collections.abc import ValuesView
from datetime import datetime
from flask.json import JSONEncoder
import json
from mongoengine.queryset import QuerySet
from pprint import pprint
from pymongo.cursor import Cursor
from uuid import UUID


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
