# This is the increment function

class Calculator:
    # This is the Calculator class

    result = 0

    def get_result(self):
        # Get Result of Calculation
        return self.result

    def add_number(self, NumA, NumB):
        # Add two numbers and store the result
        self.result = NumA + NumB
        return self.result

    def subtract_number(self, NumA, NumB):
        # Subtract two numbers and store the result
        self.result = NumA - NumB
        return self.result

    def multiply_numbers(self, NumA, NumB):
        # Multiply two numbers and store the result
        self.result = NumA * NumB
        return self.result

