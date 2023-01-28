import dataclasses
import typing as tp


@dataclasses.dataclass
class UserDTO:
    id: int
    name: str
    surname: str
    email: str
    patronymic: tp.Optional[str] = None
    phone: tp.Optional[str] = None
    is_active: bool = False


@dataclasses.dataclass
class UserRegisterDTO:
    name: str
    surname: str
    email: str
    age: int
    password: str
    patronymic: tp.Optional[str] = None
    phone: tp.Optional[str] = None


@dataclasses.dataclass
class UserLoginDTO:
    email: str
    password: str
    confirm_password: str
