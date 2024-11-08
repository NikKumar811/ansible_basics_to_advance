#!/usr/bin/python3

class FilterModule(object):
    def filters(self):
        return {
            'format_date': self.format_date,
            'sum_list': self.sum_list
        }

    def format_date(self, date_str):
        # Converts 'YYYY-MM-DD' to 'MM/DD/YYYY'
        try:
            year, month, day = date_str.split('-')
            return f"{month}/{day}/{year}"
        except ValueError:
            return "Invalid date format"

    def sum_list(self, numbers):
        # Calculates the sum of a list of numbers
        if isinstance(numbers, list) and all(isinstance(n, (int, float)) for n in numbers):
            return sum(numbers)
        return "Invalid input - requires a list of numbers"
