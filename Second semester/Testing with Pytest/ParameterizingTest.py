import pytest
import random
from ParameterizingTests import generate_random_password, SEQUENCE

@pytest.mark.parametrize('total', [6, 10, 15, 20])  # Test different lengths
def test_password_length(total):
    password = generate_random_password(total, SEQUENCE)
    assert 6 <= len(password) <= 20  # Rule 1: Check the length is within the range


@pytest.mark.parametrize('total', [8, 12, 16])
def test_password_contains_all_characters(total):
    password = generate_random_password(total, SEQUENCE)
    # Rule 2: Check for at least one uppercase character
    assert any(char.isupper() for char in password)
    # Rule 3: Check for at least one lowercase character
    assert any(char.islower() for char in password)
    # Rule 4: Check for at least one digit
    assert any(char.isdigit() for char in password)
    # Rule 5: Check for at least one special character
    assert any(char in "!@#$%^&*" for char in password)


@pytest.mark.parametrize('total', [7, 10, 18])
def test_no_repeating_characters(total):
    password = generate_random_password(total, SEQUENCE)
    # Rule 6: Ensure no more than 2 characters repeating consecutively
    assert not any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2))