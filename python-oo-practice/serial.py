"""Python serial number generator."""
print('hello')

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
    def __init__(self, start = 0):
        """set up starting number"""
        self.start = self.next = start
    
    def __repr__(self):
        """make representation more specific"""
        return f'<Serial Generator start ={self.start}, next ={self.next}>'
    
    def generate(self):
        """get the next number"""
        self.next += 1
        return self.next -1

    def reset(self):
        """Reset number to original start."""
        self.next = self.start
