import dataclasses
import typing as tp


@dataclasses.dataclass
class UserDTO:
    id: int
    name: str
    surname: str
    email: str
    patronymic: tp.Optional[str] = None
    phone: tp.Optional[int] = None
    is_active: bool = False


@dataclasses.dataclass
class UserRegisterDTO:
    name: str
    surname: str
    email: str
    patronymic: tp.Optional[str] = None
    phone: tp.Optional[int] = None
    is_active: bool = False


@dataclasses.dataclass
class UserLoginDTO:
    email: str
    password: str
    confirm_password: str
