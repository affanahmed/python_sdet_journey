import pytest
from log_parser import count_errors

def test_count_errors_basic():
    assert count_errors("ERROR abc ERROR") == 2

def test_count_errors_empty():
    assert count_errors("") == 0

def test_count_errors_none_raises():
    with pytest.raises(ValueError):
        count_errors(None)
