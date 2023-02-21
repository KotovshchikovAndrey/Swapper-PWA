# type: ignore file

from __future__ import annotations

import asyncio
import typing as tp

T = tp.TypeVar("T", bound=tp.Type[object])


class Injector:
    __instance: tp.Optional[Injector] = None
    __dependencies: tp.Dict[str, tp.Type]

    def __new__(cls, *args: tp.Any, **kwargs: tp.Any):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, dependencies: tp.Dict[str, tp.Type] = {}) -> None:
        self.__dependencies = dependencies

    def register(self, name: str):
        print(name, 11111111111)

        def decorator(dependency: T) -> T:
            dependency_instance = dependency()
            self.__dependencies[name] = dependency_instance

            return dependency

        return decorator

    def inject(self, name: str):
        dependency = self.__dependencies[name]

        def decorator(func: tp.Callable):
            def sync_wrapper(*args, **kwargs) -> tp.Any:
                dependency = self.__dependencies[name]
                args_with_dependencies = args + (dependency,)

                return func(*args_with_dependencies, **kwargs)

            async def async_wrapper(*args, **kwargs) -> tp.Any:
                dependency = self.__dependencies[name]
                args_with_dependencies = args + (dependency,)

                return await func(*args_with_dependencies, **kwargs)

            if not asyncio.iscoroutinefunction(func):
                return sync_wrapper

            return async_wrapper

        return decorator


injector = Injector()
