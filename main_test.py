import pytest
from main import validate_hours_and_mins

@pytest.mark.parametrize(
    "hour, mins, expected_response",
    [
        (5, 25, True),
        (14, 65, False)
    ]
)
def test_validate_entries__receive_hours_and_mins__return_bool(
    hour, mins, expected_response
):
    assert validate_hours_and_mins(hour, mins) == expected_response