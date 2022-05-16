"""
    :codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
import salt.modules.moosefs as moosefs


@pytest.fixture()
def configure_loader_modules():
    return {moosefs: {}}


# 'dirinfo' function tests: 1i
def test_dirinfo():
    """
    Test if it return information on a directory located on the Moose
    """
    mock = MagicMock(return_value={"stdout": "Salt:salt"})
    with patch.dict(moosefs.__salt__, {"cmd.run_all": mock}):
        assert moosefs.dirinfo("/tmp/salt") == {"Salt": "salt"}


# 'fileinfo' function tests: 1
def test_fileinfo():
    """
    Test if it returns information on a file located on the Moose
    """
    mock = MagicMock(return_value={"stdout": ""})
    with patch.dict(moosefs.__salt__, {"cmd.run_all": mock}):
        assert not moosefs.fileinfo("/tmp/salt")


# 'mounts' function tests: 1
def test_mounts():
    """
    Test if it returns a list of current MooseFS mounts
    """
    mock = MagicMock(return_value={"stdout": ""})
    with patch.dict(moosefs.__salt__, {"cmd.run_all": mock}):
        assert not moosefs.mounts()


# 'getgoal' function tests: 1
def test_getgoal():
    """
    Test if it returns goal(s) for a file or directory
    """
    mock = MagicMock(return_value={"stdout": "Salt: salt"})
    with patch.dict(moosefs.__salt__, {"cmd.run_all": mock}):
        assert moosefs.getgoal("/tmp/salt") == {"goal": "salt"}
