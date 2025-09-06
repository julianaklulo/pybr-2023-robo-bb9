import BlynkLib
from robot import Robot

robot = Robot()

BLYNK_AUTH = ""
blynk = BlynkLib.Blynk(BLYNK_AUTH)


@blynk.on("V0")
def move_forward(value):
    pressed = int(value[0])
    if pressed == 1:
        robot.move_forward()
    else:
        robot.stop()


@blynk.on("V1")
def turn_right(value):
    pressed = int(value[0])
    if pressed == 1:
        robot.turn_right()
    else:
        robot.stop()


@blynk.on("V2")
def move_backward(value):
    pressed = int(value[0])
    if pressed == 1:
        robot.move_backward()
    else:
        robot.stop()


@blynk.on("V3")
def turn_left(value):
    pressed = int(value[0])
    if pressed == 1:
        robot.turn_left()
    else:
        robot.stop()


@blynk.on("V4")
def play_sound(value):
    pressed = int(value[0])
    if pressed == 1:
        robot.play_sound()


@blynk.on("V5")
def set_angle(value):
    angle = int(value[0])
    robot.set_head_angle(angle)


@blynk.on("V6")
def set_red(value):
    intensity = int(value[0])
    robot.set_eye_color("red", intensity)


@blynk.on("V7")
def set_green(value):
    intensity = int(value[0])
    robot.set_eye_color("green", intensity)


@blynk.on("V8")
def set_blue(value):
    intensity = int(value[0])
    robot.set_eye_color("blue", intensity)


while True:
    blynk.run()
