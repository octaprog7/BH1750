# micropython
# MIT license
# Copyright (c) 2022 Roman Shevchik   goctaprog@gmail.com
import micropython
import ustruct
from sensor_pack import bus_service


class BaseSensor:
    """Base sensor class"""

    def __init__(self, adapter: bus_service.BusAdapter, address: int, big_byte_order: bool):
        """Базовый класс Датчик. если big_byte_order равен True -> порядок байтов в регистрах «big»
        (Порядок от старшего к младшему), в противном случае порядок байтов в регистрах "little"
        (Порядок от младшего к старшему)

        Base sensor class. if big_byte_order is True -> register values byteorder is 'big'
        else register values byteorder is 'little' """
        self.adapter = adapter
        self.address = address
        self.big_byte_order = big_byte_order

    def unpack(self, fmt_char: str, source: bytes) -> tuple:
        """распаковка массива, считанного из датчика.
        fmt_char: c, b, B, h, H, i, I, l, L, q, Q. pls see: https://docs.python.org/3/library/struct.html"""
        if len(fmt_char) != 1:
            raise ValueError(f"Invalid length fmt_char parameter: {len(fmt_char)}")
        if self.is_big_byteorder():
            bo = ">"    # 'big'
        else:
            bo = "<"  # 'little'
        return ustruct.unpack(bo + fmt_char, source)

    @micropython.native
    def is_big_byteorder(self) -> bool:
        return self.big_byte_order

    def get_id(self):
        raise NotImplementedError

    def soft_reset(self):
        raise NotImplementedError


class Iterator:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError
