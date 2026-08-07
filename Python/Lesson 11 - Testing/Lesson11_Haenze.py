## Python Testing 8/5/2026 Maj Shafer ##


#In Class Exercies


# Exercise 2: Test the validate_isbn() Function
# Goal: Add unit tests for the validate_isbn() function in book.py.

# This function validates ISBN format (simplified - checks for 10 or 13 digits).

# Add tests in tests/test_book.py that verify:

# Valid 10-digit ISBN returns True (e.g., "1234567890")
# Valid 13-digit ISBN returns True (e.g., "1234567890123")
# ISBN with hyphens is valid (e.g., "123-456-789-0")
# ISBN with spaces is valid (e.g., "123 456 789 0")
# Invalid formats return False:
# Too short: "123"
# Too long: "12345678901234"
# Contains letters: "12345678AB"
# Non-string input returns False (e.g., 1234567890)
# ✅ Check: All tests pass, and validate_isbn() shows 100% coverage in the report.

# Hint: You can test multiple cases in one test function or create separate test functions for each case.


def test_validate_isbn_valid_10_digit():
    """Test that valid 10-digit ISBN returns True."""
    assert validate_isbn("1234567890") is True

