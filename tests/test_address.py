import pytest

from radixdlt.address import AbstractAddress


class TestValidAddress:
    def test_is_valid(self, address):
        assert AbstractAddress.is_valid(address=address)


class TestInvalidAddress:
    @pytest.mark.parametrize("wrong_address", [b"hello world"])
    def test_is_valid(self, wrong_address):
        assert AbstractAddress.is_valid(address=wrong_address) is False
