import machine
from time import sleep


class Servo:
    """
    Servo class for controlling a servo motor using PWM signals.

    Attributes:
        _servo (machine.PWM): PWM object controlling the servo.
        _step (int): The direction of the servo sweep (1 or -1).
        _angle (int): The current angle of the servo (0 to 180 degrees).
    """

    def __init__(self, pin, angle=90):
        """
        Initialize the Servo class.

        Args:
            pin (int): The pin number to which the servo is connected.
            angle (int, optional): The initial angle for the servo (0 to 180 degrees).
        """
        self._servo = machine.PWM(machine.Pin(pin))
        self._servo.freq(50)
        self._step = 1
        self._angle = angle

    def _convert_angle_to_duty(self, angle):
        """
        Convert an angle in the range [0, 180] to a duty cycle in the range [2700, 6800].

        Args:
            angle (int): The angle to convert (0 to 180 degrees).

        Note: The duty cycle values are based on the SG90 servo motor.
        """
        duty_min = 2700
        duty_max = 6800

        angle_min = 0
        angle_max = 180

        angle_range = angle_max - angle_min
        duty_range = duty_max - duty_min

        return int((((angle - angle_min) * duty_range) / angle_range) + duty_min)

    def set_angle(self, angle):
        """
        Set the angle of the servo.

        Args:
            angle (int): The target angle (0 to 180 degrees).
        """
        duty = self._convert_angle_to_duty(angle)
        self._servo.duty_u16(duty)
        self._angle = angle

    def sweep(self, new_angle, delay=0.005):
        """
        Sweep the servo to a new angle.

        Args:
            new_angle (int): The target angle to sweep to (0 to 180 degrees).
            delay (float, optional): Time delay between each step of the sweep.
        """
        step = self._step * -1 if new_angle < self._angle else self._step

        for i in range(self._angle, new_angle, step):
            self.set_angle(i)
            sleep(delay)

        self._angle = new_angle
