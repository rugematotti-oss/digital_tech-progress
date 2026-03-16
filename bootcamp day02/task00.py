def multiply(a, b):
    return a * b

def multiply2(x):
    return x * 2

def multiply10(x):
    return x * 10

def getSecondMax(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("At least two unique numbers are required")
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


