from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "Go HIGHER!")


def test_string_secret_uses_numeric_comparison_not_lexicographic_order():
    # Regression test for the old bug where secret became a string on even attempts.
    # Numeric logic should treat 9 as lower than 10, even if secret is passed as "10".
    result = check_guess(9, "10")
    assert result == ("Too Low", "Go HIGHER!")
