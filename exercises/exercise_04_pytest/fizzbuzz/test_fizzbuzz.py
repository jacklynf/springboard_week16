import pytest

def fizzbuzz(N):
    if N % 3 == 0:
        if N % 5 == 0:
            return "fizzbuzz"
        return "fizz"
    elif N % 5 == 0:
        return "buzz"
    else:
        return N

def test_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(7) == 7
