class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = a

    def computeDifference(self):
        min_element = 101
        max_element = 0
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element

        self.maximumDifference = max_element - min_element



