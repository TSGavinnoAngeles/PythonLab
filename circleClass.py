class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        pi = 3.14
        circumference_value = pi * self.radius * 2
        return circumference_value

    def print_circumference(self):
        my_circumference = self.circumference()
        print("Circumference of a circle with a radius of " + str(self.radius) +
              " is " + str(my_circumference))


# First instantiation of the Circle class.
circle1 = Circle(2)
# Call the print_circumference method for the instantiated circle1 class.
circle1.print_circumference()

# Two more instantiations and method calls for the Circle class.
circle2 = Circle(5)
circle2.print_circumference()

circle3 = Circle(7)
circle3.print_circumference()
