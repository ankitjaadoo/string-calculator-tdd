# string_calculator.py
import re
from functools import reduce
from typing import List, Tuple

def extract_delimiter(numbers: str) -> Tuple[str, str]:
    """
    Extracts the delimiter and the numbers string from the input.
    """
    delimiter = ','
    if numbers.startswith("//"):
        parts = numbers.split('\n', 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    return delimiter, numbers

def parse_numbers(numbers: str, delimiter: str) -> List[int]:
    """
    Parses the numbers string into a list of integers based on the given delimiter.
    """
    numbers = numbers.replace('\n', delimiter)
    return list(map(int, re.split(delimiter, numbers)))

def validate_numbers(numbers: List[int]):
    """
    Validates the list of numbers, raising an error if there are negative numbers.
    """
    negatives = [num for num in numbers if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

def calculate_result(numbers: List[int], operation: str) -> int:
    """
    Calculates the result based on the given operation: '*' for multiplication, '+' for addition.
    """
    if operation == '*':
        return reduce(lambda x, y: x * y, numbers)
    else:
        return sum(numbers)

def add(numbers: str, operation: str) -> int:
    """
    Main function to calculate the result from a string of numbers with the specified operation.
    """
    if not numbers:
        return 0

    delimiter, numbers = extract_delimiter(numbers)
    num_list = parse_numbers(numbers, delimiter)
    validate_numbers(num_list)
    return calculate_result(num_list, operation)