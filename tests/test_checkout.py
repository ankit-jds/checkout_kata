import pytest
from services import Checkout

@pytest.mark.parametrize("items, expected_total", [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("CDBA", 115),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 230),
    ("AAAAAA", 260),
    ("AAAB", 160),
    ("AAABB", 175),
    ("AAABBD", 190),
    ("DABABA", 190)
])
def test_checkout_totals(items, expected_total):
    checkout = Checkout()
    for item in items:
        checkout.scan(item)
    assert checkout.total() == expected_total

def test_invalid_item():
    checkout = Checkout()
    with pytest.raises(ValueError):
        checkout.scan("X")
