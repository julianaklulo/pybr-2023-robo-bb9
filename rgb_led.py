import machine


class RGBLED:
    """
    RGBLED class for controlling a common anode or common cathode RGB LED.

    This class provides methods for setting the color of an RGB LED using either RGB color values
    or color names, allowing for easy control of the LED's color.

    Attributes:
        _red_pwm (machine.PWM): PWM object controlling the red channel of the RGB LED.
        _green_pwm (machine.PWM): PWM object controlling the green channel of the RGB LED.
        _blue_pwm (machine.PWM): PWM object controlling the blue channel of the RGB LED.
        _anode_common (bool): True if the RGB LED is common anode, False if common cathode.
    """

    def __init__(self, pin_red, pin_green, pin_blue, anode_common=True):
        """
        Initialize the RGBLED class.

        Args:
            pin_red (int): The pin number for the red channel.
            pin_green (int): The pin number for the green channel.
            pin_blue (int): The pin number for the blue channel.
            anode_common (bool, optional): True if the RGB LED is common anode, False if common cathode.
        """
        self._red_pwm = machine.PWM(machine.Pin(pin_red))
        self._red_pwm.freq(1000)

        self._green_pwm = machine.PWM(machine.Pin(pin_green))
        self._green_pwm.freq(1000)

        self._blue_pwm = machine.PWM(machine.Pin(pin_blue))
        self._blue_pwm.freq(1000)

        self._anode_common = anode_common

    def _convert_range_to_u16(self, value):
        """
        Convert a value in the range [0, 255] to a value in the range [0, 65535].

        Args:
            value (int): The value to convert.
        """
        return int((value * 65535) / 255)

    def _invert_value(self, value):
        """
        Invert a value in the range [0, 255] to a value in the range [255, 0].

        Args:
            value (int): The value to invert.
        """
        return 255 - value

    def set_color(self, red_intensity, green_intensity, blue_intensity):
        """
        Set the RGB color using a tuple (red, green, blue), where each component is in the range [0, 255].

        Args:
            red_intensity (int): The intensity value for the red channel.
            green_intensity (int): The intensity value for the green channel.
            blue_intensity (int): The intensity value for the blue channel.

        Raises:
            ValueError: If any intensity value is out of range.
        """
        rgb_colors = [red_intensity, green_intensity, blue_intensity]

        for intensity in rgb_colors:
            if not (0 <= intensity <= 255):
                raise ValueError("Intensity values should be in the range [0, 255].")

        for color, intensity in zip(["red", "green", "blue"], rgb_colors):
            color_pwm = getattr(self, f"_{color}_pwm")
            intensity = self._invert_value(intensity) if self._anode_common else intensity
            color_pwm.duty_u16(self._convert_range_to_u16(intensity))

    def set_color_by_name(self, color_name, intensity):
        """
        Set the RGB color using a color name (e.g., "red", "green", "blue")
        and an intensity value.
        The other colors remain unchanged.

        Args:
            color_name (str): The name of the color (e.g., "red", "green", "blue").
            intensity (int): The intensity value for the specified color.

        Raises:
            ValueError: If an invalid color name or intensity value is provided.
        """
        if not (0 <= intensity <= 255):
            raise ValueError("Intensity values should be in the range [0, 255].")
        
        color_pwm = getattr(self, f"_{color_name}_pwm", None)

        if color_pwm is None:
            raise ValueError(f"Invalid color name: {color_name}")

        intensity = self._invert_value(intensity) if self._anode_common else intensity
        color_pwm.duty_u16(self._convert_range_to_u16(intensity))
