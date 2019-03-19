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
