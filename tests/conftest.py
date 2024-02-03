import pytest

from edutest.app import app

@pytest.fixture()
def app_fixture():
    mocked_app = app
    mocked_app.config.update({'TESTING': True})
    yield mocked_app

@pytest.fixture
def client(app_fixture): # pylint: disable=redefined-outer-name
    yield app_fixture.test_client()
