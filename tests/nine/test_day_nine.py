import pytest

from nine.part_one_and_two import part_one, part_two

from ..utils import get_test_data

_test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            114,
            id="test data",
        ),
        get_test_data(2075724761),
    ],
)
def test_part_one(input_data: str, expected_output: int):
    assert part_one(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _test_data,
            2,
            id="test data",
        ),
        get_test_data(1072),
    ],
)
def test_part_two(input_data: str, expected_output: int):
    assert part_two(input_data) == expected_output
