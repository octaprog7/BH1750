import bus_service
from machine import Pin
from typing import Union


class BaseSensor:
    """Base sensor class"""
    def __init__(self, adapter: bus_service.BusAdapter, address: Union[int, Pin]):
        self.adapter = adapter
        self.address = address

    def get_id(self):
        raise NotImplementedError

    def soft_reset(self):
        raise NotImplementedError


class Iterator:
    """Для поддержки получения данных от датчика с помощью итератора"""
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError
