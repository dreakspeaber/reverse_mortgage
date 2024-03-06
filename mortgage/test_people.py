import pytest
from mortgage import People  # Update the import path according to your project structure

# Test case for initializing People with valid age
def test_people_init_valid_age():
    person = People(age=70)
    assert person.age == 70
    assert person.max_claim == 0  # assuming max_claim is set later
    assert person._errors == {}

# Test case for checking is_valid method with age below MIN_AGE
def test_people_is_valid_below_min_age():
    person = People(age=60)
    assert person.is_valid() is False
    assert "min_age" in person._errors

# Test case for getting max_claim based on age
@pytest.mark.parametrize("age,expected_max_claim", [
    (24, 0),
    (62, 38),
    (70, 50),
    (80, 60),
    (90, 80),
])
def test_get_max_claim(age, expected_max_claim):
    person = People(age=age)
    assert person.get_max_claim() == expected_max_claim
    assert person.max_claim == expected_max_claim

# Test case for checking errors returned when age is valid
def test_people_errors_empty_on_valid_age():
    person = People(age=70)
    person.is_valid()
    assert person.errors() == {}
