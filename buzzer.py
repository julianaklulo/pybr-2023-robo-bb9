import machine
from time import sleep


class Buzzer:
    """
    Buzzer class for controlling a simple buzzer.

    Attributes:
        _buzzer (machine.PWM): PWM object controlling the buzzer.
    """

    def __init__(self, pin):
        """
        Initialize the Buzzer class with a pin for buzzer control.

        Args:
            pin (int): The pin number for controlling the buzzer.
        """
        self._buzzer = machine.PWM(machine.Pin(pin))
        self._buzzer.freq(500)
        self._buzzer.duty_u16(0)

    def play(self, frequency, duration=1):
        """
        Play a sound with the buzzer for a specified duration.

        Args:
            frequency (int): The frequency of the sound.
            duration (float, optional): The duration to play the sound (in seconds).
        """
        self._buzzer.duty_u16(frequency)
        sleep(duration)
        self._buzzer.duty_u16(0)
