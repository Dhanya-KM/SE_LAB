
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


def test_withdraw_account_branches():
    with pytest.raises(ValueError):
        withdraw(20000, 1000, "business", True)

    assert withdraw(20000, 1000, "savings", True) == 19000


def test_withdraw_amount_branches():
    with pytest.raises(ValueError):
        withdraw(20000, -100, "savings", True)

    with pytest.raises(ValueError):
        withdraw(20000, 150, "savings", True)

    assert withdraw(20000, 100, "savings", True) == 19900


def test_withdraw_limit_branches():
    assert withdraw(50000, 25100, "savings", True) == "limit exceeded"
    assert withdraw(50000, 25000, "savings", True) == 25000


def test_withdraw_bank_branches():
    assert withdraw(20000, 1000, "savings", True) == 19000
    assert withdraw(20000, 1000, "savings", False) == 18980
    assert withdraw(20000, 11000, "current", False) == 8970


def test_withdraw_balance_branches():
    assert withdraw(1000, 2000, "savings", True) == "insufficient funds"
    assert withdraw(20000, 5000, "savings", True) == 15000
    assert withdraw(1010, 1000, "savings", False) == "insufficient funds"


def test_pin_attempt_branches():
    assert pin_check(1234, 1234, 3) == "card blocked"
    assert pin_check(1234, 1234, 0) == "ok"
    assert pin_check(1111, 1234, 2) == "card blocked"
    assert pin_check(1111, 1234, 1) == "retry"


def test_note_breakup_branches():
    with pytest.raises(ValueError):
        note_breakup(150)

    assert note_breakup(700) == (1, 1, 0)
    assert note_breakup(600) == (1, 0, 1)
    assert note_breakup(500) == (1, 0, 0)
