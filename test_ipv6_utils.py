import unittest
from ipv6_utils import minimal_subnet_from_ips
from common_utils import read_ip_addresses_from_file


class TestIPv6Utils(unittest.TestCase):
    def test_minimal_subnet_single_ip(self):
        ip_addresses = read_ip_addresses_from_file("data/ipv6_single_ip.txt")
        self.assertEqual(minimal_subnet_from_ips(ip_addresses), "ffe0::80:0:0:0/128")

    def test_minimal_subnet_multiple_ips(self):
        ip_addresses = read_ip_addresses_from_file("data/ipv6_multiple_ips.txt")
        self.assertEqual(minimal_subnet_from_ips(ip_addresses), "ffe0::/72")

    def test_minimal_subnet_empty_file(self):
        ip_addresses = read_ip_addresses_from_file("data/empty_ips.txt")
        self.assertEqual(minimal_subnet_from_ips(ip_addresses), '')

    def test_minimal_subnet_invalid_ips(self):
        ip_addresses = read_ip_addresses_from_file("data/ipv6_addresses_invalid.txt")
        with self.assertRaises(ValueError):
            minimal_subnet_from_ips(ip_addresses)


if __name__ == '__main__':
    unittest.main()
