from sensor_pack import bus_service


class BaseSensor:
    """Base sensor class"""

    def __init__(self, adapter: bus_service.BusAdapter, address: int):
        self.adapter = adapter
        self.address = address

    def get_id(self):
        raise NotImplementedError

    def soft_reset(self):
        raise NotImplementedError


class Iterator:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError
