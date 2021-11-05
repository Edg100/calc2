"""This is the increment function"""

class Calculator:
    """This is the Calculator class"""

    result = 0

    def get_result(self):
        """Get Result of Calculation"""
        return self.result

    def add_numbers(self, num_a, num_b):
        """Add two num_bers and store the result"""
        self.result = num_a + num_b
        return self.result

    def subtract_numbers(self, num_a, num_b):
        """Subtract two num_bers and store the result"""
        self.result = num_a - num_b
        return self.result

    def multiply_numbers(self, num_a, num_b):
        """Multiply two num_bers and store the result"""
        self.result = num_a * num_b
        return self.result
