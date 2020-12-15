# from madlib_cli import __version__

import pytest
from madlib_cli.madlib import read_template, parse_template

# , merge


def test_read_template_returns_stripped_string():
    actual = read_template("madlib_cli/madlib.txt")
    expected = "We are going to have fun with madlibs today. Please input the following:\n"
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "What are a {Large Animal} and backpacking {Small Animal} to do?"
    )
    expected_stripped = "What are a {} and backpacking {} to do?"
    expected_parts = ("Large Animal", "Small Animal")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# def test_merge():
#     actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
#     expected = "It was a dark and stormy night."
#     assert actual == expected


# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "missing.txt"
#         read_template(path)