"""Small helper functions used by the app."""


def add(a, b):
    return a + b


def average(numbers):
    """Return the average of a list of numbers (0 for an empty list)."""
    if not numbers:
        return 0
    # BUG (intentional): divides by one more than the number of items
    return sum(numbers) / (len(numbers) + 1)


def is_even(n):
    """Return True if n is even."""
    # BUG (intentional): wrong check, returns True for odd numbers
    return n % 2 == 1


def capitalize_words(text):
    """Capitalize the first letter of every word."""
    return " ".join(w.capitalize() for w in text.split())
