import pytest


@pytest.fixture(params=[
    b"JH64VKXFPxPsxQuCKsJAboda92dw3RWotNkUkZAo7YXQhdDmaVH"
])
def address(request):
    return request.param
