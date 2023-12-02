from pathlib import Path
from typing import Iterator

import pytest

import one.part_one
import one.part_two

_input_data = (Path(__file__).parent / "data" / "input_data.txt").open().readlines()


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip().split(
                "\n"
            ),
            142,
            id="test data",
        ),
        pytest.param(
            _input_data,
            55002,
            id="challenge data",
        ),
    ],
)
def test_part_one(input_data: Iterator[str], expected_output: int):
    assert one.part_one.sum_all_values(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip().split(
                "\n"
            ),
            281,
            id="test data",
        ),
        pytest.param(
            _input_data,
            55093,
            id="challenge data",
        ),
    ],
)
def test_part_two(input_data: Iterator[str], expected_output: int):
    assert one.part_two.sum_all_values(input_data) == expected_output
