from typing import Iterator

_filter_numbers = list(map(str, range(10)))


def get_first_and_last_values_of_line(input_line: str) -> int:
    only_integers = list(filter(_filter_numbers.__contains__, input_line))
    if len(only_integers) == 1:
        only_integers *= 2
    return int(only_integers[0]) * 10 + int(only_integers[-1])


def sum_all_values(input_lines: Iterator[str]) -> int:
    return sum(map(get_first_and_last_values_of_line, input_lines))
