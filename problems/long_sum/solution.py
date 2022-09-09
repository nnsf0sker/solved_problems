from itertools import zip_longest
from typing import List


def long_sum(first_number: List[int], second_number: List[int], base: int) -> List[int]:
    """
    Sum of two numbers represented as arrays
    :param first_number: Array represents the first number to sum
    :param second_number: Array represents the second number to sum
    :param base: Numeral system base
    :return: Array represents the sum of two numbers
    """
    result = []
    prev_remainder = 0
    for first_number_digit, second_number_digit in zip_longest(first_number, second_number, fillvalue=0):
        result.append((first_number_digit + second_number_digit + prev_remainder) % base)
        prev_remainder = (first_number_digit + second_number_digit) // base
    if prev_remainder:
        result.append(prev_remainder)
    return result


if __name__ == "__main__":
    assert long_sum([0], [0], base=10) == [0]
    assert long_sum([0], [1], base=10) == [1]
    assert long_sum([1], [0], base=10) == [1]
    assert long_sum([1], [1], base=10) == [2]
    assert long_sum([1, 0], [0], base=10) == [1, 0]
    assert long_sum([0], [1, 0], base=10) == [1, 0]
    assert long_sum([1, 1], [1, 1], base=10) == [2, 2]
    assert long_sum([1, 2, 3], [3, 2, 1], base=10) == [4, 4, 4]
    assert long_sum([4, 1], [1, 9], base=10) == [5, 0, 1]
