import requests
from typing import Optional
from warcio import ArchiveIterator

from models.document import Document
from parsers.html.parser import HtmlDocumentParser

class CommonCrawlArchive:
    def __init__(
        self,
        path: str,
        data_base_url: str
    ):
        self.path = path
        self.data_base_url = data_base_url
        self._records = None

    def fetch_records(self):
        if self._records is None:
            response = requests.get(
                f"{self.data_base_url}/{self.path}",
                stream=True
            )

            self._records = ArchiveIterator(response.raw)

        return self._records

    def get_response_document(self) -> Optional[Document]:
        records = self.fetch_records()

        for record in records:
            if record.rec_type == "response":
                data = record.content_stream().read()
                parser = HtmlDocumentParser()

                return parser.parse(
                    data=data,
                    url=record.rec_headers.get_header("WARC-Target-URI"),
                    source_ip_addr=record.rec_headers.get_header("WARC-IP-Address")
                )

        return None