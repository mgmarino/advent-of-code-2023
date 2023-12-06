from typing import Iterator

import pytest

from six.part_one_and_two import Race, part_one_and_two


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            [
                Race(time_of_race=7, record_distance=9),
                Race(time_of_race=15, record_distance=40),
                Race(time_of_race=30, record_distance=200),
            ],
            288,
            id="test data, part one",
        ),
        pytest.param(
            [
                Race(time_of_race=49, record_distance=263),
                Race(time_of_race=97, record_distance=1532),
                Race(time_of_race=94, record_distance=1378),
                Race(time_of_race=94, record_distance=1851),
            ],
            4403592,
            id="challenge data, part one",
        ),
        pytest.param(
            [
                Race(time_of_race=71530, record_distance=940200),
            ],
            71503,
            id="test data, part two",
        ),
        pytest.param(
            [
                Race(time_of_race=49979494, record_distance=263153213781851),
            ],
            38017587,
            id="challenge data, part two",
        ),
    ],
)
def test_part_one(input_data: Iterator[Race], expected_output: int):
    assert part_one_and_two(input_data) == expected_output
