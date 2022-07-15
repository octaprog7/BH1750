import base_sensor
import bus_service
import ustruct


class Bhv1750(base_sensor.BaseSensor):
    """Class for work with ambient Light Sensor BHV1750"""

    def _send_cmd(self, command: int):
        """send 1 byte command to device"""
        self.adapter.write(self.address, command.to_bytes(1))

    def get_id(self):
        return None

    def soft_reset(self):
        self._send_cmd(0b0000_0111)

    def power(self, on_off: bool = True):
        if on_off:
            self._send_cmd(0b0000_0001)
        else:
            self._send_cmd(0b0000_0000)

    def set_mode(self, continuously: bool, high_resolution: bool = True):
        """Set sensor mode"""
        cmd = 0
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
