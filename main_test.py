import pytest
import builtins
from unittest import mock
from main import validate_hours_and_mins, user_prompt, time_in_words

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

def test_validate_input():
    mock_numbers = (x for x in [5, 25])
    with mock.patch.object(builtins, 'input', side_effect = mock_numbers):
        assert user_prompt() == (5, 25)

def test_validate_entrie_receives_hours_equals_to_number_word():
    assert time_in_words(5, None) == "five"
    assert time_in_words(6, None) == "six"