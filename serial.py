"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        "Create serial number starting with 100"
        self.current = start

    def generate(self):
        "Generate serial number"
        serial_number = self.current
        self.current += 1
        return serial_number
    
    def reset(self, start=100):
        "Reset serial number to original starting value"
        self.current = start
