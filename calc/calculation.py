"""This is our calculation base class / Abstract Class"""
class Calculation:
    """contstructor and it is the first function called
     when an object of the class is instantiated"""
    def __init__(self,num_a, num_b):
        """self references the instantiated object of the class
        these are instance properties that are being sharred
        with the child classes (addition, subtraction, etc...)"""
        self.num_a = num_a
        self.num_b = num_b
    @classmethod
    def create(cls, num_a, num_b):
        return cls(num_a,num_b)
