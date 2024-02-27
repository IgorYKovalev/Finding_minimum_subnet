import ipaddress
from typing import List
from timeit_decorator import timeit


@timeit
def minimal_subnet_from_ips_bitwise(ip_addresses: List[str]) -> str:
    """
    Возвращает минимальную подсеть для списка IPv4 адресов с использованием побитовых операций.
    """
    if not ip_addresses:
        return ''

    # Фильтрация и валидация IP-адресов
    ips = []
    for ip_str in ip_addresses:
        try:
            ips.append(int(ipaddress.IPv4Address(ip_str)))
        except ipaddress.AddressValueError as e:
            raise ValueError(f"Невалидный IP-адрес: {ip_str}") from e

    min_ip = min(ips)
    max_ip = max(ips)

    # Находим общий префикс с использованием побитовых операций
    diff = min_ip ^ max_ip
    mask_length = 32
    while diff:
        diff >>= 1
        mask_length -= 1

    # Создаем и возвращаем строку подсети
    subnet = ipaddress.IPv4Network((min_ip, mask_length), strict=False)
    return f"{subnet.with_prefixlen}"
