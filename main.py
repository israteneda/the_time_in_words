"""
https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true
"""
hours = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}

def validate_hours_and_mins(hour: int, minutes: int):
    """
    Validate hours and minutes
    """
    return (1 <= hour <= 12) and (0 <= minutes < 60)

def user_prompt():
    hours = input()
    minutes = input()
    return (hours, minutes)

def time_in_words(h,m):
    return hours[h]