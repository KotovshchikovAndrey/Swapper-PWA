import typing as tp


class IUser:
    id: int
    name: str
    email: str
    password: str
    phone: tp.Optional[str] = None
    is_active: bool = False


class IToken:
    id: int
    user: IUser
    value: str


class ICode:
    id: int
    user: IUser
    value: int
