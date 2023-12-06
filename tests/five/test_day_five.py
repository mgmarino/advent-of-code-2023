from pathlib import Path
from typing import Iterator

import pytest

from five.part_one import part_one

_input_data = (Path(__file__).parent / "data" / "input_data.txt").open().readlines()
_test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split(
    "\n"
)


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            35,
            id="test data",
        ),
        pytest.param(
            _input_data,
            107430936,
            id="challenge data",
        ),
    ],
)
def test_part_one(input_data: Iterator[str], expected_output: int):
    assert part_one(input_data) == expected_output
