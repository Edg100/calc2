"""This is the increment function"""

class Calculator:
    """This is the Calculator class"""

    result = 0

    def get_result(self):
        """Get Result of Calculation"""
        return self.result

    def add_num_ber(self, num_a, num_b):
        """Add two num_bers and store the result"""
        self.result = num_a + num_b
        return self.result

    def subtract_num_ber(self, num_a, num_b):
        """Subtract two num_bers and store the result"""
        self.result = num_a - num_b
        return self.result

    def multiply_num_bers(self, num_a, num_b):
        """Multiply two num_bers and store the result"""
        self.result = num_a * num_b
        return self.result
