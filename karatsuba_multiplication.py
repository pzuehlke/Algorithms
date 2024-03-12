# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def karatsuba(x: int, y: int):
    """
    Multiplies two nonnegative integers using the Karatsuba multiplication
    algorithm.
    Parameters:
        * x, y (int): Nonnegative integers to be multiplied.

    Returns:
        * (int): The product of x and y.
    """
    # Convert to strings for easy splitting:
    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))

    # Adjust the length of numbers so that they are equal and even:
    n = n if n % 2 == 0 else n + 1
    str_x = str_x.zfill(n)
    str_y = str_y.zfill(n)

    # Base case:
    if n <= 2:
        return x * y

    mid = n // 2
    a, b = int(str_x[:mid]), int(str_x[mid:])
    c, d = int(str_y[:mid]), int(str_y[mid:])

    # Recursive calls:
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Karatsuba formula:
    product = (10**n) * ac + (10**mid) * ad_plus_bc + bd
    return product


# Examples:
if __name__ == '__main__':
    test_cases = [
        (1234, 5678),  # Simple case
        (12345, 67890),  # Larger numbers
        (12, 345),  # Different lengths
        (0, 1234),  # Multiplying by zero
        (9999, 9999),  # Multiplying same large numbers
        (123456789, 987654321),  # Very large numbers
        (1111, 2222),  # Numbers with repeating digits
        (1, 2),  # Small numbers
        (123, 0),  # Zero on the right
    ]

    for x, y in test_cases:
        product = karatsuba(x, y)
        print(f"The product of {x} and {y} is {product}")
        assert product == x * y, f"Test failed for input: {x}, {y}"

    print("All test cases passed successfully!")
