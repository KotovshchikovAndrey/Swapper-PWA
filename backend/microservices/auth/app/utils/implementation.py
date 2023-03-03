import typing as tp

T = tp.TypeVar("T", bound=tp.Type[object])


class Implement(tp.Generic[T]):
    def __init__(self, interface: object) -> None:
        self.__interface = interface

    def __call__(self, cls: T) -> T:
        implement_attrs = self.__interface.__dict__["__annotations__"]
        for attr, attr_type in implement_attrs.items():
            if cls.__dict__.get(attr) is None:
                raise NotImplementedError(
                    f"Атрибут {attr} типа {attr_type} должен быть имлементирован!"
                )

        return cls
