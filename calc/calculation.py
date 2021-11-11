"""Calculation base class or Abstract Class"""
class Calculation:
    """This is called constructor"""
    def __init__(self,num_a, num_b):
        """self  represents the object inside the class that are being shared
        with the child classes (addition, subtraction, etc...)"""
        self.num_a = num_a
        self.num_b = num_b
    @classmethod
    def create(cls, num_a, num_b):
        """This is to return the two values to calculation parent class"""
        return cls(num_a, num_b)
