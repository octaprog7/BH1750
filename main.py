# micropython
# mail: goctaprog@gmail.com
# MIT license


# Please read this before use!: https://www.ti.com/product/TMP117
from machine import I2C
import bhv1750
from sensor_pack.bus_service import I2cAdapter
import time

if __name__ == '__main__':
    # пожалуйста установите выводы scl и sda в конструкторе для вашей платы, иначе ничего не заработает!
    # please set scl and sda pins for your board, otherwise nothing will work!
    # https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
    # i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=400_000) № для примера
    # bus =  I2C(scl=Pin(4), sda=Pin(5), freq=100000)   # на esp8266    !
    i2c = I2C(0, freq=400_000)  # on Arduino Nano RP2040 Connect tested
    adaptor = I2cAdapter(i2c)
    # ps - pressure sensor
    sol = bhv1750.Bhv1750(adaptor, 0x23)

    # если у вас посыпались исключения, чего у меня на макетной плате с али и проводами МГТВ не наблюдается,
    # то проверьте все соединения.
    # Радиотехника - наука о контактах! РТФ-Чемпион!
    sol.power(True)     # Sensor Of Lux
    sol.set_mode(True, True)
    curr_max = 0
    
    for lux in sol:
        time.sleep_ms(150)
        curr_max=max(lux, curr_max)
        print(f"Current illumination [lux]: {lux}\tNormalized [%]: {int(100*lux/curr_max)}")
