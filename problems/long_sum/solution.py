from typing import Generator
from itertools import zip_longest


def long_sum(
        first_number: Generator[int or bytes, None, None],
        second_number: Generator[int or bytes, None, None],
        base: int
) -> Generator[int or bytes, None, None]:
    """
    Sum of two array-numbers
    :param first_number: Array represents the first number to sum
    :param second_number: Array represents the second number to sum
    :param base: Numeral system base
    :return: Array represents the sum of two numbers
    """
    prev_remainder = 0
    for first_number_digit, second_number_digit in zip_longest(first_number, second_number, fillvalue=0):
        yield (first_number_digit + second_number_digit + prev_remainder) % base
        prev_remainder = (first_number_digit + second_number_digit) // base
    if prev_remainder:
        yield prev_remainder


if __name__ == "__main__":
    def long_sum_assert(
            first_number: Generator[int or bytes, None, None],
            second_number: Generator[int or bytes, None, None],
            base: int,
            expected_result: Generator[int or bytes, None, None]
    ) -> None:
        long_sum_tuple_result = tuple(
            long_sum((elem for elem in first_number), (elem for elem in second_number), base=base)
        )
        expected_tuple_result = tuple(expected_result)
        assert long_sum_tuple_result == expected_tuple_result, f"{long_sum_tuple_result} != {expected_tuple_result}"
    long_sum_assert(b'\x00', b'\x00', 10, b'\x00')  # 0 + 0 = 0
    long_sum_assert(b'\x00', b'\x01', 10, b'\x01')  # 0 + 1 = 1
    long_sum_assert(b'\x01', b'\x00', 10, b'\x01')  # 1 + 0 = 1
    long_sum_assert(b'\x01', b'\x01', 10, b'\x02')  # 1 + 1 = 2
    long_sum_assert(b'\x00', b'\x00\x01', 10, b'\x00\x01')  # 0 + 10 = 10
    long_sum_assert(b'\x01\x01', b'\x01\x01', 10, b'\x02\x02')  # 11 + 11 = 22
    long_sum_assert(b'\x01\x02\x03', b'\x03\x02\x01', 10, b'\x04\x04\x04')  # 321 + 123 = 444
    long_sum_assert(b'\x04\x01', b'\x01\x09', 10, b'\x05\x00\x01')  # 14 + 91 = 105
