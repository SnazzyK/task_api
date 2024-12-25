import pytest


@pytest.fixture()
def load_test():
    print("load test")


@pytest.fixture()
def api_only_test():
    print("load test api")
