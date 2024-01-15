#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        self._page_count = None  # Use a private variable to store the page_count
        self.title = title

        # Set the page_count property to ensure it's an integer
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Check if the value is an integer before setting it
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        if self.page_count > 0:
            print("Flipping the page...wow, you read fast!")

# Example usage:
book = Book("And Then There Were None", 272)
book.page_count = "not an integer"
