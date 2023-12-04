from pathlib import Path
from typing import Iterator

import pytest

from four.part_one_and_two import part_one, part_two

_input_data = (Path(__file__).parent / "data" / "input_data.txt").open().readlines()
_test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip().split(
    "\n"
)


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            13,
            id="test data",
        ),
        pytest.param(
            _input_data,
            25183,
            id="challenge data",
        ),
    ],
)
def test_part_one(input_data: Iterator[str], expected_output: int):
    assert part_one(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            30,
            id="test data",
        ),
        pytest.param(
            _input_data,
            5667240,
            id="challenge data",
        ),
    ],
)
def test_part_two(input_data: Iterator[str], expected_output: int):
    assert part_two(input_data) == expected_output
