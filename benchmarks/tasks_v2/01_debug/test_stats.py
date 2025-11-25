
import pytest
from stats_util import calculate_median
def test_median_odd(): assert calculate_median([1, 3, 5]) == 3
def test_median_even(): assert calculate_median([1, 2, 3, 4]) == 2.5
def test_empty(): assert calculate_median([]) is None
