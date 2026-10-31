
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


def test_withdraw_valid_own_bank():
    assert withdraw(20000, 5000, "savings", True) == 15000


def test_withdraw_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(20000, 1000, "business", True)


def test_withdraw_invalid_zero_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(20000, 0, "savings", True)


def test_withdraw_invalid_non_multiple():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(20000, 150, "savings", True)


def test_withdraw_limit_exceeded():
    assert withdraw(50000, 25100, "savings", True) == "limit exceeded"


def test_withdraw_non_own_bank():
    assert withdraw(20000, 1000, "savings", False) == 18980


def test_withdraw_non_own_bank_high_amount():
    assert withdraw(20000, 11000, "current", False) == 8970


def test_withdraw_insufficient_funds():
    assert withdraw(1000, 2000, "savings", True) == "insufficient funds"


def test_withdraw_insufficient_funds_with_fee():
    assert withdraw(1010, 1000, "savings", False) == "insufficient funds"


def test_pin_correct():
    assert pin_check(1234, 1234, 0) == "ok"


def test_pin_wrong_retry():
    assert pin_check(1111, 1234, 0) == "retry"


def test_pin_blocked_third_attempt():
    assert pin_check(1111, 1234, 2) == "card blocked"


def test_pin_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"


def test_note_breakup_valid():
    assert note_breakup(800) == (1, 1, 1)


def test_note_breakup_invalid():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(150)


def test_note_breakup_without_200_notes():
    assert note_breakup(600) == (1, 0, 1)
