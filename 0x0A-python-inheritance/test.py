#!/usr/bin/python3

class Example:
    def __init__(self, data):
        self.data = data

    def sort_data(self):
        self.data = sorted(self.data)

# Usage
example_instance = Example([3, 1, 4, 1, 5, 9, 2])
print("Original Data:", example_instance.data)

example_instance.sort_data()
print("Sorted Data:", example_instance.data)

