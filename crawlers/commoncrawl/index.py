import requests
import gzip
from typing import List
from datetime import datetime

from crawlers.commoncrawl.archive import CommonCrawlArchive

class CommonCrawlIndex:
    def __init__(
        self,
        id: str,
        start_date: datetime,
        end_date: datetime,
        data_base_url: str
    ):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.data_base_url = data_base_url

    def get_archives(self) -> List[CommonCrawlArchive]:
        compressed_data = requests.get(
            f"{self.data_base_url}/crawl-data/{self.id}/warc.paths.gz"
        ).content

        data = gzip.decompress(compressed_data)
        lines = list(map(lambda line: line.decode("utf-8"), data.splitlines()))
        archives = []

        for line in lines:
            archives.append(CommonCrawlArchive(
                path=line,
                data_base_url=self.data_base_url
            ))

        return archives