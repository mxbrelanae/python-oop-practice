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

    def __init__(self, start=0):
        """Start Generator."""

        self.start = self.next = start

    def __repr__(self):
        """A reference the Start point and next number generated ."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Returns the next int."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets int to start point."""

        self.next = self.start
