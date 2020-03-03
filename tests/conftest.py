import os

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="function")
def testclient():

    with TestClient(app) as client:
        # Application 'startup' handlers are called on entering the block.
        yield client
    # Application 'shutdown' handlers are called on exiting the block.
