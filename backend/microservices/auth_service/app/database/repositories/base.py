import typing as tp
from abc import ABC

import ormar

T = tp.TypeVar("T", bound=ormar.Model)


class BaseSqlRepository(ABC, tp.Generic[T]):
    _model: tp.Type[T]

    def __init__(self, model: tp.Type[T]) -> None:
        self._model = model

    async def get_all(self) -> tp.Iterable[T]:
        return await self._model.objects.all()

    async def get_by_id(self, id: tp.Union[int, str]) -> tp.Optional[T]:
        return await self._model.objects.get_or_none(id=id)
