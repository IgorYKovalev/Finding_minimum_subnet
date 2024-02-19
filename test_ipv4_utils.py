import unittest
from ipv4_utils import minimal_subnet_from_ips
from common_utils import read_ip_addresses_from_file


class TestIPv4Utils(unittest.TestCase):
    def test_minimal_subnet_single_ip(self):
        ip_addresses = read_ip_addresses_from_file("data/ipv4_single_ip.txt")
        self.assertEqual(minimal_subnet_from_ips(ip_addresses), "192.168.1.1/32")

    def test_minimal_subnet_multiple_ips(self):
        ip_addresses = read_ip_addresses_from_file("data/ipv4_multiple_ips.txt")
        self.assertEqual(minimal_subnet_from_ips(ip_addresses), "192.168.1.0/29")

    def test_minimal_subnet_empty_file(self):
        ip_addresses = read_ip_addresses_from_file("data/empty_ips.txt")
        self.assertEqual(minimal_subnet_from_ips(ip_addresses), '')

    def test_minimal_subnet_invalid_ips(self):
        ip_addresses = read_ip_addresses_from_file("data/ipv4_addresses_invalid.txt")
        with self.assertRaises(ValueError):
            minimal_subnet_from_ips(ip_addresses)


if __name__ == '__main__':
    unittest.main()
