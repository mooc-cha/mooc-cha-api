import os
import pytest

from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    db_url = 'postgres://postgres:@localhost/mooc_cha_{}'
    initializer(["rating.models"], db_url=db_url, app_label='rating')
    request.addfinalizer(finalizer)

