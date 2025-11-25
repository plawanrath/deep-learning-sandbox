
import pytest
from stats_util import calculate_median

def test_median_odd():
    assert calculate_median([1, 3, 5]) == 3
    assert calculate_median([5, 1, 3]) == 3

def test_median_even():
    # For [1, 2, 3, 4], median is (2+3)/2 = 2.5
    assert calculate_median([1, 2, 3, 4]) == 2.5

def test_empty():
    assert calculate_median([]) is None
