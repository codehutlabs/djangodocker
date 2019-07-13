from website.utils import add
import pytest


class TestUtils:
    def test_add(self):

        assert add(1, 2) == 3, "1 + 2 should equal 3"
