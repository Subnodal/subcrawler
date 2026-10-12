import requests
from typing import Optional, List
from datetime import datetime

from models.crawler import Crawler
from models.document import Document
from crawlers.commoncrawl.index import CommonCrawlIndex

class CommonCrawl(Crawler):
    CRAWL_INDEX_URL = "https://index.commoncrawl.org/collinfo.json"
    DATA_BASE_URL = "https://data.commoncrawl.org"

    def __init__(self):
        super().__init__()

        self.crawl_index_url = self.CRAWL_INDEX_URL
        self.data_base_url = self.DATA_BASE_URL

    def get_crawl_indexes(self) -> List[CommonCrawlIndex]:
        data = requests.get(self.crawl_index_url).json()
        indexes = []

        for entry in data:
            indexes.append(CommonCrawlIndex(
                id=entry["id"],
                start_date=datetime.fromisoformat(entry["from"]),
                end_date=datetime.fromisoformat(entry["to"]),
                data_base_url=self.data_base_url
            ))

        indexes.sort(key=lambda index: index.end_date, reverse=True)

        return indexes

    def crawl_next(self) -> Optional[Document]:
        first_index = self.get_crawl_indexes()[0]
        first_archive = first_index.get_archives()[0]
        document = first_archive.get_response_document()

        return document