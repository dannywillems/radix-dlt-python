import pytest


@pytest.fixture(params=[
    b"JH64VKXFPxPsxQuCKsJAboda92dw3RWotNkUkZAo7YXQhdDmaVH",
    b"JHB89drvftPj6zVCNjnaijURk8D8AMFw4mVja19aoBGmRXWchnJ"
])
def address(request):
    return request.param
