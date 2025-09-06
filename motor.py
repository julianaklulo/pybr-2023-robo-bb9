import machine


class Motor:
    """
    Motor class for controlling a DC motor with two pins.

    Attributes:
        _pin_a (machine.Pin): Pin A for controlling the motor.
        _pin_b (machine.Pin): Pin B for controlling the motor.
    """

    def __init__(self, pin_a, pin_b):
        """
        Initialize the Motor class with two pins.

        Args:
            pin_a (int): The pin number for one terminal of the motor).
            pin_b (int): The pin number for the other terminal of the motor).
        """
        self._pin_a = machine.Pin(pin_a, machine.Pin.OUT)
        self._pin_b = machine.Pin(pin_b, machine.Pin.OUT)

    def forward(self):
        """
        Turn the motor forward.
        """
        self._pin_a.value(1)
        self._pin_b.value(0)

    def backward(self):
        """
        Turn the motor backward.
        """
        self._pin_a.value(0)
        self._pin_b.value(1)

    def stop(self):
        """
        Stop the motor.
        """
        self._pin_a.value(0)
        self._pin_b.value(0)
