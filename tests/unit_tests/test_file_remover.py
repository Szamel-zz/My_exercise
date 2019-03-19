from MockTraining.file_remover import rm


import os
import mock
import unittest
print(type(rm))

class RmTestCase(unittest.TestCase):
    @mock.patch('MockTraining.file_remover.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")


@mock.patch("os.listdir", mock.MagicMock(return_value="test1"))
def test1():
    assert "test1" == os.listdir()

@mock.patch("os.listdir")
def test2(mock_listdir):
    mock_listdir.return_value = "test2"
    assert "test2" == os.listdir()

@mock.patch("os.listdir")
class Test():
    def not_decorated_and_not_tested(self):
        assert False
    def test3(self, mock_listdir):
        mock_listdir.return_value = "test3"
        assert "test3" == os.listdir()