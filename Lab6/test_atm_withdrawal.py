import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


def test_withdraw():
    assert withdraw(20000, 5000, "savings", True) == 15000


def test_pin_check():
    assert pin_check(1234, 1234, 0) == "ok"


def test_note_breakup():
    assert note_breakup(800) == (1, 1, 1)