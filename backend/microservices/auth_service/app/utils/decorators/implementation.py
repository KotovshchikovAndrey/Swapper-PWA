import typing as tp
from abc import ABC

from errors.implement_errors import ImplementError


class Implement:
    def __init__(self, interface: object) -> None:
        self.__interface = interface

    def __call__(self, cls: tp.Callable):
        implement_attrs = self.__interface.__dict__["__annotations__"]
        for attr, attr_type in implement_attrs.items():
            if cls.__dict__.get(attr) is None:
                raise ImplementError(
                    message=f"Атрибут {attr} типа {attr_type} должен быть имлементирован!"
                )

        return cls
