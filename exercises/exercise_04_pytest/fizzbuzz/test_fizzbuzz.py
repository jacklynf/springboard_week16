import pytest

golden_data = [
    (15, "fizzbuzz"),
    (3, "fizz"),
    (5, "buzz"),
    (7, 7),
    (12, "fizz"),
    (20, "buzz"),
    (30, "fizzbuzz"),
    (100, "buzz"),
    (101, 101),
]

@pytest.fixture(params=golden_data)
def my_fixture(request):
    return request.param

def fizzbuzz(N):
    if N % 15 == 0:
        return "fizzbuzz"
    elif N % 3 == 0:
        return "fizz"
    elif N % 5 == 0:
        return "buzz"
    else:
        return N

def test_fizzbuzz(my_fixture):
    input_val, output = my_fixture
    assert fizzbuzz(input_val) == output
    
