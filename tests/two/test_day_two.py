from typing import Iterator

import pytest

from two.part_one_and_two import Cubes, part_one, part_two

from ..utils import get_test_data

_test_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()
_max_cubes = Cubes(red=12, green=13, blue=14)


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            8,
            id="test data",
        ),
        get_test_data(2416),
    ],
)
def test_part_one(input_data: Iterator[str], expected_output: int):
    assert part_one(input_data.split("\n"), _max_cubes) == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            2286,
            id="test data",
        ),
        get_test_data(63307),
    ],
)
def test_part_two(input_data: Iterator[str], expected_output: int):
    assert part_two(input_data.split("\n")) == expected_output
