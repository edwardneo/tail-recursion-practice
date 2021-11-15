import pytest

from fact import *
from exp import *
from fib import *
from real import *

class TestFactorial:
    """Factorial function tests"""

    def test_one(self):
        assert fact(1) == fact_tr(1)
    
    def test_five(self):
        assert fact(5) == fact_tr(5)
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            fact(1000)
    
    def test_frame_limit(self):
        fact_tr(1000)

class TestExp:
    """Power function tests"""

    def test_one(self):
        assert exp(2, 1) == exp_tr(2, 1)
    
    def test_five(self):
        assert exp(2, 5) == exp_tr(2, 5)
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            exp(2, 1000)
    
    def test_frame_limit(self):
        exp_tr(2, 1000)

class TestFibonacci:
    """Fibonacci function tests"""

    def test_one(self):
        assert fib(1) == fib_tr(1)
    
    def test_five(self):
        assert fib(5) == fib_tr(5)
    
    def test_frame_limit(self):
        fib_tr(500)

class TestReal:
    """Int to float function tests"""

    def test_one(self):
        assert real(1) == real_tr(1)
    
    def test_five(self):
        assert real(5) == real_tr(5)
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            real(1000)
    
    def test_frame_limit(self):
        real_tr(1000)