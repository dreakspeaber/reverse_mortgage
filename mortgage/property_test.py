import pytest
from mortgage import Property  

# Test initializing Property with valid value
def test_property_init_valid_value():
    property = Property(value=15000)
    assert property.value == 15000
    assert property._errors == {}

# Test validation for Property value below the minimum
def test_property_is_valid_below_min():
    property = Property(value=9000)
    assert property.is_valid() is False
    assert "value" in property._errors
    assert property._errors['value'] == "Property value must be greater than  10000."

# Test validation for Property with valid value
def test_property_is_valid_above_min():
    property = Property(value=11000)
    assert property.is_valid() is True
    assert property._errors == {}

# Test retrieving Property value
def test_get_property_value():
    property_value = 20000
    property = Property(value=property_value)
    assert property.get_value() == property_value

# Test errors method when no errors are present
def test_property_errors_empty_on_valid_value():
    property = Property(value=15000)
    property.is_valid()  # Trigger validation
    assert property.errors() == {}
