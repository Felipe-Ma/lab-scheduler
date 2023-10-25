import unittest
from functions import *
from unittest.mock import patch, Mock


# Test the functions
class TestFunctions(unittest.TestCase):

    # Test get_username()
    @patch("functions.os.getenv", side_effect=Exception("Mocked exception"))
    @patch("functions.print")
    def test_get_username_exception(self, mock_print, mock_getenv):
        result = get_username()
        # Check if exception message is printed
        mock_print.assert_called_with("Mocked exceptionError getting username!")

        # Check if the function returns the default value
        self.assertEqual(result, "Unknown")

    def test_get_username(self):
        self.assertEqual(get_username(), "fmartine")

    # Test get_ip()
    # Test exception
    @patch("functions.socket.socket", side_effect=Exception("Mocked exception"))
    @patch("functions.print")
    def test_get_ip_exception(self, mock_print, mock_socket):
        result = get_ip()
        mock_print.assert_called_with("Mocked exceptionError getting IP address!")
        self.assertEqual(result, "Unknown")

    def test_get_ip(self):
        self.assertEqual(get_ip(), "10.248.200.191")

