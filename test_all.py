import pytest
import time

def some_func(args):
    time.sleep(0.1)



def test_my_case(benchmark):
    benchmark(some_func, ())

