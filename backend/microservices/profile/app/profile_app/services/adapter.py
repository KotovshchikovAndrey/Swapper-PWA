import typing as tp
from abc import ABC, abstractmethod

import requests


class IApiAdapter(ABC):
    host: str

    @abstractmethod
    def read(self, url: str) -> tp.Mapping[str, tp.Any]:
        raise NotImplementedError()

    @abstractmethod
    def write(self, url: str) -> tp.Mapping[str, tp.Any]:
        raise NotImplementedError()


class RestApiAdapter(IApiAdapter):
    def __init__(self, host: str) -> None:
        self.host = host

    def read(self, url: str, **kwargs: tp.Any):
        response = requests.get(url=f"{self.host}/{url}", params=kwargs, timeout=60)
        return response.json()

    def write(self, url: str, **kwargs: tp.Any):
        response = requests.post(url=f"{self.host}/{url}", data=kwargs, timeout=60)
        return response.json()


class ApiAdapterFactory:
    adapters = {
        "rest": RestApiAdapter,
    }

    @classmethod
    def create(cls, adapter_type: str, host: str) -> IApiAdapter:
        adapter = cls.adapters.get(adapter_type)
        return adapter(host)
