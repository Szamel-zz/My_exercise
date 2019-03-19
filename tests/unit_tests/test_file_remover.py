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


class RmTestCase(unittest.TestCase):

    @mock.patch('MockTraining.file_remover.os.path')
    @mock.patch('MockTraining.file_remover.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False

        rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        rm("any path")

        mock_os.remove.assert_called_with("any path")

