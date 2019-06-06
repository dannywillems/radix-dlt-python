import pytest

from radixdlt.address import AbstractAddress


class TestValidAddress:
    def test_is_valid(self, address):
        assert AbstractAddress.is_valid(address=address)
    #
    # @pytest.mark.parametrize("address,expected_public_key", [
    #     (b"JH64VKXFPxPsxQuCKsJAboda92dw3RWotNkUkZAo7YXQhdDmaVH", b"")
    # ])
    # def test_from_string(self, address, expected_public_key):
    #     assert AbstractAddress.from_string(address=address) == expected_public_key


class TestInvalidAddress:
    @pytest.mark.parametrize("wrong_address", [b"hello world"])
    def test_is_valid(self, wrong_address):
        assert AbstractAddress.is_valid(address=wrong_address) is False
