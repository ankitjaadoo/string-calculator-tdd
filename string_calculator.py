# string_calculator.py
def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace('\n', ',')
    num_list = map(int, numbers.split(','))
    return sum(num_list)