"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(value):
    """Check if a given value is a palindrome using deque."""
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    if value == "":  # Fix: Return False for empty strings
        return False

    cleaned_value = "".join(value.lower().split())  # Normalize input
    char_deque = deque(cleaned_value)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

