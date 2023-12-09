import inspect
from pathlib import Path

import pytest
from _pytest.mark.structures import ParameterSet


def get_test_data(expected_value) -> ParameterSet:
    marks = tuple()
    _challenge_data = None
    try:
        _challenge_data = (
            (Path(inspect.stack()[1].filename).parent / "data" / "input_data.txt")
            .open()
            .read()
        )
    except FileNotFoundError:
        marks = pytest.mark.skip("No available data")

    return pytest.param(
        _challenge_data, expected_value, id="challenge data", marks=marks
    )
