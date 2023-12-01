from pathlib import Path
from typing import Iterator

_filter_numbers = list(map(str, range(10)))


def get_first_and_last_values_of_line(input_line: str) -> int:
    only_integers = list(filter(_filter_numbers.__contains__, input_line))
    if len(only_integers) == 1:
        only_integers *= 2
    return int(only_integers[0]) * 10 + int(only_integers[-1])


def sum_all_values(input_lines: Iterator[str]) -> int:
    return sum(map(get_first_and_last_values_of_line, input_lines))


test_data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()

test_result = 142

if __name__ == "__main__":
    assert sum_all_values(test_data.split("\n")) == test_result
    print(sum_all_values((Path(__file__).parent / "input_data.txt").open().readlines()))
