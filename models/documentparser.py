from typing import Optional
from abc import ABC, abstractmethod
from ipaddress import IPv4Address, IPv6Address

from models.document import Document

class DocumentParser(ABC):
    @abstractmethod
    def parse(
        self,
        data,
        url: str,
        source_ip_addr: Optional[IPv4Address | IPv6Address] = None
    ) -> Document:
        pass