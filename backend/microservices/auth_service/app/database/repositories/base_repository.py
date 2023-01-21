import typing as tp
from abc import ABC

import ormar

T = tp.TypeVar("T", bound=tp.Type[ormar.Model])


class BaseSqlRepository(ABC, tp.Generic[T]):
    _model: T

    def __init__(self, model: T) -> None:
        self._model = model

    async def get_all(self) -> tp.Iterable[T]:
        return await self._model.objects.all()

    async def get_by_id(self, id: tp.Union[int, str]) -> T:
        return await self._model.objects.get(id=id)

    async def delete(self, id: tp.Union[int, str]) -> None:
        await self._model.objects.delete(id=id)
