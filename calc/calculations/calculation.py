"""Calculation Class or Abstract Class"""
class Calculation:
    # pylint: disable=too-few-public-methods

#self  represents the object inside the class that are being shared.
    def __init__(self,values: tuple):
        """This is called constructor method"""
        self.values = Calculation.conv_args_list_flt(values)
    @staticmethod
    def conv_args_list_flt(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
