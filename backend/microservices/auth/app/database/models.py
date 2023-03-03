import ormar

from core import entities
from database.connections import get_connection
from utils.implementation import Implement

database_connection = get_connection()


class BaseMeta(ormar.ModelMeta):
    metadata = database_connection.metadata
    database = database_connection.database


@Implement(interface=entities.UserEntity)  # type: ignore
class User(ormar.Model):
    class Meta(BaseMeta):  # type: ignore
        tablename = "user"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=100, nullable=False)
    email = ormar.String(max_length=100, unique=True, nullable=False)
    password = ormar.String(max_length=255, nullable=False)
    phone = ormar.String(max_length=18, nullable=True)
    is_active = ormar.Boolean(default=False, index=True)


@Implement(interface=entities.TokenEntity)  # type: ignore
class Token(ormar.Model):
    class Meta(BaseMeta):  # type: ignore
        tablename = "token"

    id = ormar.Integer(primary_key=True)
    user = ormar.ForeignKey(User, nullable=False)
    value = ormar.String(max_length=255, unique=True, nullable=False)


@Implement(interface=entities.CodeEntity)  # type: ignore
class Code(ormar.Model):
    class Meta(BaseMeta):  # type: ignore
        tablename = "code"

    id = ormar.Integer(primary_key=True)
    user = ormar.ForeignKey(User, unique=True, nullable=False)
    value = ormar.SmallInteger(minimum=1000, maximum=9999)
