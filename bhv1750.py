from sensor_pack.base_sensor import BaseSensor, Iterator
import sys
import ustruct


class Bhv1750(BaseSensor, Iterator):
    """Class for work with ambient Light Sensor BHV1750"""

    def __del__(self):
        self.power(False)   # power off before delete

    def _send_cmd(self, command: int):
        """send 1 byte command to device"""
        self.adapter.write(self.address, command.to_bytes(1, sys.byteorder))

    def get_id(self):
        """No ID support in sensor!"""
        return None

    def soft_reset(self):
        """Software reset."""
        self._send_cmd(0b0000_0111)

    def power(self, on_off: bool = True):
        """Sensor powering"""
        if on_off:
            self._send_cmd(0b0000_0001)
        else:
            self._send_cmd(0b0000_0000)

    def set_mode(self, continuously: bool, high_resolution: bool = True):
        """Set sensor mode.
        high resolution mode 2 not implemented. I have no desire to do this!"""
        if continuously:
            cmd = 0b0001_0000  # continuously mode
        else:
            cmd = 0b0010_0000  # one shot mode

        if not high_resolution:
            cmd |= 0b11    # L-Resolution Mode

        self._send_cmd(cmd)

    def get_illumination(self) -> int:
        """Return illumination in lux"""
        tmp = self.adapter.read(self.address, 2)
        return int(ustruct.unpack(">H", tmp)[0])

    def __next__(self) -> int:
        return self.get_illumination()
