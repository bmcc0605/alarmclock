import RPi.GPIO as gpio

class Light:
    pinNumber = -1

    def __init__(self, pinNum):
        gpio.setmode(gpio.BCM)
        self.pinNumber = pinNum
        gpio.setup(self.pinNumber, gpio.OUT)

    def __del__(self):
        self.disable()

    def enable(self):
        gpio.output(self.pinNumber, gpio.HIGH)

    def disable(self):
        gpio.output(self.pinNumber, gpio.LOW)
