import pytest
from string_calculator import StringCalculator

def test_add_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.Add("") == 0

def test_add_single_number_returns_number():
    calc = StringCalculator()
    assert calc.Add("1") == 1

def test_add_two_numbers_comma_separated():
    calc = StringCalculator()
    assert calc.Add("1,2") == 3

def test_add_multiple_numbers():
    calc = StringCalculator()
    assert calc.Add("1,2,3") == 6

def test_add_newline_delimiter():
    calc = StringCalculator()
    assert calc.Add("1\n2,3") == 6

def test_add_negative_numbers_raises_exception():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="negatives not allowed: -1, -2"):
        calc.Add("-1,-2,3")

def test_add_ignore_numbers_greater_than_1000():
    calc = StringCalculator()
    assert calc.Add("2,1001") == 2

def test_add_custom_delimiter():
    calc = StringCalculator()
    assert calc.Add("//;\n1;2") == 3

def test_add_long_delimiter():
    calc = StringCalculator()
    assert calc.Add("//[***]\n1***2***3") == 6

def test_add_multiple_delimiters():
    calc = StringCalculator()
    assert calc.Add("//[*][%]\n1*2%3") == 6