from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset shared in-memory activity state between tests."""
    app_module.activities = deepcopy(_INITIAL_ACTIVITIES)


@pytest.fixture
def client():
    return TestClient(app_module.app)
