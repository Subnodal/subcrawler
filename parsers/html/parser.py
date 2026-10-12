from typing import Optional
from ipaddress import IPv4Address, IPv6Address

from models.document import Document
from models.documentparser import DocumentParser

class HtmlDocumentParser(DocumentParser):
    def parse(
        self,
        data: bytes,
        url: str,
        source_ip_addr: Optional[IPv4Address | IPv6Address] = None
    ) -> Document:
        return Document(
            url=url,
            title="",
            body="",
            source_ip_addr=source_ip_addr
        )