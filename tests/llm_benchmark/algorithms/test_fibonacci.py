import pytest
from llm_benchmark.algorithms.fibonacci import Fibonacci

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (15, 610),
    ],
)
def test_nth_fibonacci(n, expected):
    assert Fibonacci.nth_fibonacci(n) == expected


def test_nth_fibonacci_negative():
    with pytest.raises(ValueError):
        Fibonacci.nth_fibonacci(-1)


@pytest.mark.parametrize(
    "n, expected_seq",
    [
        (0, [0]),
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2]),
        (5, [0, 1, 1, 2, 3, 5]),
        (10, [0, 1, 1, 2, 3, 5, 8]),
        (20, [0, 1, 1, 2, 3, 5, 8, 13]),
    ],
)
def test_fibonacci_sequence(n, expected_seq):
    assert Fibonacci.fibonacci_sequence(n) == expected_seq


def test_fibonacci_sequence_negative():
    with pytest.raises(ValueError):
        Fibonacci.fibonacci_sequence(-5) 