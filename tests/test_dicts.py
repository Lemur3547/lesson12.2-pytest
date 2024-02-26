import pytest

from utils import dicts


@pytest.fixture
def data():
    return {"vcs": "mercurial"}


def test_get_val(data):
    assert dicts.get_val(data, "vcs")
    assert dicts.get_val(data, "vcs", "git")
    assert dicts.get_val({}, "vcs", "git")
    assert dicts.get_val({}, "vcs", "bazaar")
