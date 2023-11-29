import pytest
from main import DateTime  

# Test cases for DateTime class methods
def test_valid_date():
    assert DateTime.is_valid_date(29, 2, 2020) == True  
    assert DateTime.is_valid_date(31, 12, 2023) == True

    assert DateTime.is_valid_date(29, 2, 2021) == False  
    assert DateTime.is_valid_date(30, 2, 2023) == False  
    assert DateTime.is_valid_date(1, 1, 1) == True  
    assert DateTime.is_valid_date(31, 12, 9999) == True 

    with pytest.raises(TypeError):
        DateTime.is_valid_date("test", 5, 2023)

def test_date_difference():
    dt1 = DateTime(2023, 11, 1)
    dt2 = DateTime(2023, 11, 15)

    assert DateTime.calculate_date_difference(dt2, dt1) == 14

    with pytest.raises(TypeError):
        DateTime.calculate_date_difference(123, "abc")

