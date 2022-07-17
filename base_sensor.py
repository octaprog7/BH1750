from bus_service import BusAdapter


class BaseSensor:
    """Base sensor class"""

    def __init__(self, adapter: BusAdapter, address: int):
        self.adapter = adapter
        self.address = address

    def get_id(self):
        pass

    def soft_reset(self):
        pass


class Iterator:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError
