import pytest

from app_name import helpers
from app_name import db


def test_something():
    assert helpers.helper_f()
    assert db.create_db()
    test_list = [1]
    with pytest.raises(IndexError):
        x = test_list[1]
        print(x)
