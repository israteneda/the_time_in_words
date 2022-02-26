"""
https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true
"""


def validate_hours_and_mins(hour: int, minutes: int):
    """
    Validatet hours and minutes
    """
    return (1 <= hour <= 12) and (0 <= minutes < 60)