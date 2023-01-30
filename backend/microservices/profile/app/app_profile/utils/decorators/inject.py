import functools
import typing as tp


class Inject:
    __injectable_cls: tp.Type[object]
    __name: str

    def __init__(
        self, cls: tp.Type[object], name: str = "service", *args, **kwargs
    ) -> None:
        self.__injectable_cls = cls
        self.__name = name
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self, func: tp.Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            kwargs[self.__name] = self.__injectable_cls(*self.__args, *self.__kwargs)
            return func(*args, **kwargs)

        return wrapper
