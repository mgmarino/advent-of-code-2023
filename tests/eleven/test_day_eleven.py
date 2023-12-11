import pytest

from eleven.part_one_and_two import part_one_and_two

from ..utils import get_test_data

_test_data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            (_test_data, 2),
            374,
            id="test data, scale 2",
        ),
        pytest.param(
            (_test_data, 10),
            1030,
            id="test data, scale 10",
        ),
        pytest.param(
            (_test_data, 100),
            8410,
            id="test data, scale 100",
        ),
        get_test_data(9521776, 2),
        get_test_data(553224415344, 1000000),
    ],
)
def test_part_one_and_two(input_data: tuple[str, int], expected_output: int):
    assert part_one_and_two(*input_data) == expected_output
