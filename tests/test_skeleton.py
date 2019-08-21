# -*- coding: utf-8 -*-

import pytest
from describe_variable.skeleton import fib

__author__ = "Miguel Alcalde"
__copyright__ = "Miguel Alcalde"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
