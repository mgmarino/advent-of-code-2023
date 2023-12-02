import re
from pathlib import Path
from typing import Iterator

text_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
} | {str(i): i for i in range(10)}

_regex = re.compile("|".join(f"{c}" for c in text_mapping.keys()))


def get_first_and_last_values_of_line(input_line: str) -> int:
    def _func() -> Iterator[str]:
        for i in range(len(input_line)):
            if not (val := _regex.search(input_line[i:])):
                return
            yield val.group(0)

    find_values = list(_func())
    if len(find_values) == 1:
        find_values *= 2
    return text_mapping[find_values[0]] * 10 + text_mapping[find_values[-1]]


def sum_all_values(input_lines: Iterator[str]) -> int:
    return sum(map(get_first_and_last_values_of_line, input_lines))


test_data = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()

test_result = 281

if __name__ == "__main__":
    assert sum_all_values(test_data.split("\n")) == test_result
    print(sum_all_values((Path(__file__).parent / "input_data.txt").open().readlines()))
