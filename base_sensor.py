from abc import ABC, abstractmethod

from bus_service import BusAdapter


class BaseSensor(ABC):
    """Base sensor class"""

    def __init__(self, adapter: BusAdapter, address: int):
        self.adapter = adapter
        self.address = address

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def soft_reset(self):
        pass
