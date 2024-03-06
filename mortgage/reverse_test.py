import pytest
from mortgage import ReverseMortgageManager  # Adjust import as necessary

# Test initializing ReverseMortgageManager with valid inputs
def test_reverse_mortgage_manager_init():
    manager = ReverseMortgageManager(age=70, property_value=500000)
    assert manager.people.age == 70
    assert manager.prop.value == 500000
    assert manager._errors == {}

# Test is_valid method when both people and property are valid
def test_is_valid_both_valid():
    manager = ReverseMortgageManager(age=70, property_value=500000)
    assert manager.is_valid() is True
    assert manager._errors == {}

# Test is_valid method when one or both are invalid
@pytest.mark.parametrize("age,property_value,expected", [
    (61, 500000, False),  # Age below minimum
    (70, 9000, False),  # Property value below minimum
    (61, 9000, False)  # Both below minimum
])
def test_is_valid_with_invalid_inputs(age, property_value, expected):
    manager = ReverseMortgageManager(age=age, property_value=property_value)
    assert manager.is_valid() == expected

# Test get_max_cap functionality
@pytest.mark.parametrize("property_value,expected", [
    (500000, 500000),  # Property value below MAX_CAP
    (1500000, 1000000)  # Property value above MAX_CAP
])
def test_get_max_cap(property_value, expected):
    manager = ReverseMortgageManager(age=70, property_value=property_value)
    assert manager.get_max_cap() == expected

# Assuming People.get_max_claim and Property.get_value work correctly,
# a simplified test for get_principal_limit (exact calculations might vary)
def test_get_principal_limit():
    manager = ReverseMortgageManager(age=70, property_value=500000)
    principal_limit = manager.get_principal_limit()
    assert isinstance(principal_limit, dict)
    # Perform specific assertions based on expected calculation results
