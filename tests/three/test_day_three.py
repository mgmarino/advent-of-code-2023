from pathlib import Path
from typing import Iterator

import pytest

from three.part_one_and_two import part_one, part_two

_input_data = (Path(__file__).parent / "data" / "input_data.txt").open().readlines()
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
""".strip().split(
    "\n"
)


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            4361,
            id="test data",
        ),
        pytest.param(
            _input_data,
            522726,
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
            467835,
            id="test data",
        ),
        pytest.param(
            _input_data,
            81721933,
            id="challenge data",
        ),
    ],
)
def test_part_two(input_data: Iterator[str], expected_output: int):
    assert part_two(input_data) == expected_output
