import time
from buzzer import Buzzer
from rgb_led import RGBLED
from servo import Servo
from motor import Motor


class Robot:
    """
    Robot class for controlling the robot.

    Attributes:
        _motor_left (Motor): The left motor.
        _motor_right (Motor): The right motor.
        _servo (Servo): The servo motor.
        _led (RGBLED): The RGB LED.
        _buzzer (Buzzer): The buzzer.
    """
    def __init__(self):
        """
        Initialize the Robot class.
        """
        self._motor_left = Motor(3, 2)
        self._motor_right = Motor(4, 5)
        self._servo = Servo(6)
        self._led = RGBLED(8, 9, 10)
        self._buzzer = Buzzer(12)

        self.startup()

    def startup(self):
        """
        Perfom a sequence of commands to indicate that the robot is ready.
        """
        self._led.set_color(0, 0, 0)

        # Blink the LED red 5 times
        for _ in range(5):
            self.set_eye_color("red", 255)
            time.sleep(0.5)
            self.set_eye_color("red", 0)
            time.sleep(0.5)

        # Turn the LED blue
        self.set_eye_color("blue", 255)

        # Turn the head from left to right
        self.set_head_angle(90)
        self.set_head_angle(0)
        self.set_head_angle(180)
        self.set_head_angle(90)

        # Turn the LED green
        self.set_eye_color("green", 255)

        # Play a sound
        self.play_sound()

    def move_forward(self):
        self._motor_left.forward()
        self._motor_right.forward()

    def move_backward(self):
        self._motor_left.backward()
        self._motor_right.backward()

    def turn_left(self):
        self._motor_left.forward()
        self._motor_right.backward()

    def turn_right(self):
        self._motor_left.backward()
        self._motor_right.forward()

    def stop(self):
        self._motor_left.stop()
        self._motor_right.stop()

    def set_head_angle(self, angle):
        self._servo.sweep(angle)

    def set_eye_color(self, color, intensity):
        self._led.set_color_by_name(color, intensity)

    def play_sound(self):
        for _ in range(5):
            self._buzzer.play(500, 0.5)
            time.sleep(0.2)
