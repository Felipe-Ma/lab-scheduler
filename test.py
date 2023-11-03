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
        self.assertEqual(get_username(), "Felipe")

    # Test get_ip()
    # Test exception
    @patch("functions.socket.socket", side_effect=Exception("Mocked exception"))
    @patch("functions.print")
    def test_get_ip_exception(self, mock_print, mock_socket):
        result = get_ip()
        mock_print.assert_called_with("Mocked exceptionError getting IP address!")
        self.assertEqual(result, "Unknown")

    def test_get_ip(self):
        self.assertEqual(get_ip(), "10.0.0.10")

    # Test get_os()
    # Test exception
    @patch("functions.platform.platform", side_effect=Exception("Mocked exception"))
    @patch("functions.print")
    def test_get_os_exception(self, mock_print, mock_platform):
        result = get_os()
        mock_print.assert_called_with("Mocked exceptionError getting Operating System!")
        self.assertEqual(result, "Unknown")

    def test_get_os(self):
        self.assertEqual(get_os(), "Windows-10")

    # Test get_cpu()
    # Test exception
    @patch("functions.cpuinfo.get_cpu_info", side_effect=Exception("Mocked exception"))
    @patch("functions.print")
    def test_get_cpu_exception(self, mock_print, mock_cpuinfo):
        result = get_cpu()
        mock_print.assert_called_with("Mocked exceptionError getting CPU info!")
        self.assertEqual(result, "Unknown")

    def test_get_cpu(self):
        self.assertEqual(get_cpu(), "AMD Ryzen 5 5600X 6-Core Processor")

    # Test get_product_name()
    # Test exception
    @patch("functions.subprocess.Popen", side_effect=Exception("Mocked exception"))
    @patch("functions.print")
    def test_get_product_name_exception(self, mock_print, mock_wmi):
        result = get_product_name()
        mock_print.assert_called_with("Mocked exceptionError getting Product Name!")
        self.assertEqual(result, "Unknown")

    def test_get_product(self):
        self.assertEqual(get_product_name(), "System Product Name")
