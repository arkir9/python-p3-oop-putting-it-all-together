#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition='New'):
        self.brand = brand
        self._size = None  # Use a private variable to store the size

        # Set the size property to ensure it's an integer
        self.size = size

        self.condition = condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Check if the value is an integer before setting it
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")


stan_smith = Shoe("Adidas", 9)
stan_smith.size = "not an integer"
