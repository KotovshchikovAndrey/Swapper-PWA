import typing as tp

import ormar

from database.connections import postgresql_connection


class BaseMeta(ormar.ModelMeta):
    metadata = postgresql_connection.metadata
    database = postgresql_connection.database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=100, nullable=False)
    surname = ormar.String(max_length=100, nullable=False)
    patronymic = ormar.String(max_length=100, nullable=True)
    email = ormar.String(max_length=100, nullable=False)
    phone = ormar.String(max_length=18)


class Token(ormar.Model):
    class Meta(BaseMeta):
        tablename = "token"

    id = ormar.Integer(primary_key=True)
    user = ormar.ForeignKey(User, nullable=False)
    value = ormar.String(max_length=255, unique=True, nullable=False)


class Code(ormar.Model):
    class Meta(BaseMeta):
        tablename = "code"

    id = ormar.Integer(primary_key=True)
    user = ormar.ForeignKey(User, unique=True, nullable=False)
    value = ormar.SmallInteger(minimum=1000, maximum=9999)
