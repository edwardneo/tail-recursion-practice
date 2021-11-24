import pytest

from fact import *
from exp import *
from fib import *
from real import *
from sum_list import *
from concat_2d_list import *
from combine_ord_lists import *
from minimum import *
from reverse_list import *
from count_hailstone import *
from maximum import *
from create_range import *
from find_fringe import *

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

class TestSumList:
    """Sum list function tests"""

    def test_one(self):
        assert sum_list([1]) == sum_list_tr([1])
    
    def test_five(self):
        assert sum_list([1, 2, 3, 4, 5]) == sum_list_tr([1, 2, 3, 4, 5])
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            sum_list([1] * 1000)
    
    def test_frame_limit(self):
        sum_list_tr([1] * 1000)

class TestConcat2DList:
    """Concatenating lists inside a list function tests"""

    def test_one(self):
        assert concat_2d_list([[1, 2]]) == concat_2d_list_tr([[1, 2]])
    
    def test_five(self):
        assert concat_2d_list([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == concat_2d_list_tr([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            concat_2d_list([[1]] * 1000)
    
    def test_frame_limit(self):
        concat_2d_list_tr([[1]] * 1000)
    
class TestCombineOrdList:
    """Combining ordered lists function tests"""

    def test_one(self):
        assert combine_ord_lists([1], [2]) == combine_ord_lists_tr([1], [2])
    
    def test_five(self):
        assert combine_ord_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == combine_ord_lists_tr([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    
    def test_key(self):
        assert combine_ord_lists([10, 8, 6, 4, 2], [9, 7, 5, 3, 1], lambda x: -x) == combine_ord_lists_tr([10, 8, 6, 4, 2], [9, 7, 5, 3, 1], lambda x: -x)

    def test_max_frames(self):
        with pytest.raises(RecursionError):
            combine_ord_lists(list(range(1, 1000, 2)), list(range(2, 1001, 2)))
    
    def test_frame_limit(self):
        combine_ord_lists_tr(list(range(1, 1000, 2)), list(range(2, 1001, 2)))

class TestMinimum:
    """Minimum function tests"""

    def test_one(self):
        assert minimum([1]) == minimum_tr([1])
    
    def test_five(self):
        assert minimum([5, 4, 3, 2, 1]) == minimum_tr([5, 4, 3, 2, 1])
    
    def test_key(self):
        assert minimum([1, 2, 3, 4, 5], lambda x: -x) == minimum_tr([1, 2, 3, 4, 5], lambda x: -x)
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            minimum(list(range(1000, 0, -1)))
    
    def test_frame_limit(self):
        minimum_tr(list(range(1000, 0, -1)))

class TestReverseList:
    """List reversal function tests"""

    def test_one(self):
        assert reverse_list([1]) == reverse_list_tr([1])
    
    def test_five(self):
        assert reverse_list([1, 2, 3, 4, 5]) == reverse_list_tr([1, 2, 3, 4, 5])
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            reverse_list(list(range(1, 1001)))
    
    def test_frame_limit(self):
        reverse_list_tr(list(range(1, 1001)))

class TestCountHailstone:
    """Hailstone length function tests"""

    def test_one(self):
        assert count_hailstone(1) == count_hailstone_tr(1)
    
    def test_five(self):
        assert count_hailstone(5) == count_hailstone_tr(5)
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            count_hailstone(9780657630)
    
    def test_frame_limit(self):
        count_hailstone_tr(9780657630)

class TestMaximum:
    """Maximum function tests"""

    def test_one(self):
        assert maximum([1]) == maximum_tr([1])
    
    def test_five(self):
        assert maximum([1, 2, 3, 4, 5]) == maximum_tr([1, 2, 3, 4, 5])
    
    def test_key(self):
        assert maximum([5, 4, 3, 2, 1], lambda x: -x) == maximum_tr([5, 4, 3, 2, 1], lambda x: -x)
    
    def test_max_frames(self):
        with pytest.raises(RecursionError):
            maximum(list(range(1000, 0, -1)))
    
    def test_frame_limit(self):
        maximum_tr(list(range(1000, 0, -1)))

class TestCreateRange:
    """Range function tests"""

    def test_one(self):
        assert create_range(0, 1) == create_range_tr(0, 1)
    
    def test_five(self):
        assert create_range(0, 5) == create_range_tr(0, 5)
    
    def test_interval(self):
        assert create_range(10, 0, -2) == create_range_tr(10, 0, -2)
    
    def test_one_arg(self):
        assert create_range(10) == create_range_tr(10)

    def test_max_frames(self):
        with pytest.raises(RecursionError):
            create_range(0, 1000)

    def test_frame_limit(self):
        create_range_tr(0, 1000)

class TestFindFringe:
    """Find fringe function tests"""

    def test_one(self):
        tree = Tree(1, fringe=True)
        assert find_fringe(tree) == find_fringe_tr(tree)
    
    def test_five(self):
        tree = Tree(1, [Tree(2), Tree(3, [Tree(4, fringe=True), Tree(5, fringe=True)], fringe=True)])
        assert find_fringe(tree) == find_fringe_tr(tree)
    
    def test_max_frame(self):
        tree = self.create_1000_tree()
        with pytest.raises(RecursionError):
            find_fringe(tree)
    
    def test_frame_limit(self):
        tree = self.create_1000_tree()
        find_fringe_tr(tree)
    
    def create_1000_tree(self):
        tree = Tree(0)
        tree_count = tree
        for i in range(1, 1500):
            tree_count.branches = [Tree(i, fringe=(i>1400))]
            tree_count = tree_count.branches[0]
        return tree
            
