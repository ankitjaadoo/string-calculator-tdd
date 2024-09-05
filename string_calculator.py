# string_calculator.py
import re
from functools import reduce

def add(numbers: str, character: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ','
    
    if numbers.startswith("//"):
        parts = numbers.split('\n', 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    
    numbers = numbers.replace('\n', delimiter)
    num_list = list(map(int, re.split(delimiter, numbers)))
    
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    
    if character == '*':
        product = reduce(lambda x, y: x * y, num_list)
        return product
    else:
        return sum(num_list)