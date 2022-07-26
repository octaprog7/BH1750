# micropython
# MIT license
# Copyright (c) 2022 Roman Shevchik   goctaprog@gmail.com
"""service class for I/O bus operation"""
from machine import I2C, SPI, Pin
from typing import Union


class BusAdapter:
    """Proxy between I/O bus and device I/O class"""
    def __init__(self, bus: Union[I2C, SPI]):
        self.bus = bus

    def read_register(self, device_addr: int, reg_addr: int, bytes_count: int = 2):
        """считывает из регистра датчика значение.
        bytes_count - размер значения в байтах"""
        raise NotImplementedError

    def write_register(self, device_addr: int, reg_addr: int, value: int,
                       bytes_count: int = 2, byte_order: str = "big"):
        """записывает данные value в датчик, по адресу reg_addr.
        bytes_count - кол-во записываемых данных"""
        raise NotImplementedError

    def read(self, device_addr, n_bytes: int) -> bytes:
        """Read n_bytes from the peripheral specified by device_addr"""
        raise NotImplementedError

    def write(self, device_addr, buf: bytes):
        """Write the bytes from buf to the peripheral specified by device_addr"""
        raise NotImplementedError


class I2cAdapter(BusAdapter):
    def __init__(self, bus: I2C):
        super().__init__(bus)

    def write_register(self, device_addr: int, reg_addr: int, value: int,
                       bytes_count: int = 2, byte_order: str = "big"):
        """записывает данные value регистр датчика, по адресу reg_addr.
        bytes_count - кол-во записываемых данных"""
        buf = value.to_bytes(bytes_count, byte_order)
        return self.bus.writeto_mem(device_addr, reg_addr, buf)

    def read_register(self, device_addr: int, reg_addr: int, bytes_count: int = 2):
        """считывает из регистра датчика значение.
        bytes_count - размер значения в байтах"""
        return self.bus.readfrom_mem(device_addr, reg_addr, bytes_count)

    def read(self, device_addr, n_bytes: int) -> bytes:
        return self.bus.readfrom(device_addr, n_bytes)

    def write(self, device_addr, buf: bytes):
        return self.bus.writeto(device_addr, buf)
