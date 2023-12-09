from typing import Iterator

import pytest

from three.part_one_and_two import part_one, part_two

from ..utils import get_test_data

_test_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            4361,
            id="test data",
        ),
        get_test_data(522726),
    ],
)
def test_part_one(input_data: Iterator[str], expected_output: int):
    assert part_one(input_data.split("\n")) == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            467835,
            id="test data",
        ),
        get_test_data(81721933),
    ],
)
def test_part_two(input_data: Iterator[str], expected_output: int):
    assert part_two(input_data.split("\n")) == expected_output
