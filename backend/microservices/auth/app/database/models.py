import ormar

from core import entities
from database import postgres
from utils.decorators.implementation import Implement


class BaseMeta(ormar.ModelMeta):
    metadata = postgres.metadata
    database = postgres.database


@Implement(interface=entities.UserEntity)  # type: ignore
class User(ormar.Model):
    class Meta(BaseMeta):  # type: ignore
        tablename = "user"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=100, nullable=False)
    surname = ormar.String(max_length=100, nullable=False)
    patronymic = ormar.String(max_length=100, nullable=True)
    email = ormar.String(max_length=100, unique=True, nullable=False)
    password = ormar.String(max_length=255, nullable=False)
    age = ormar.Integer(maximum=100, nullable=False)
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
