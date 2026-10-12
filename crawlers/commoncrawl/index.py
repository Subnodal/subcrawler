import requests
import gzip
from typing import List
from datetime import datetime

from commoncrawl.segment import CommonCrawlSegment

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

    def get_segments(self) -> List[CommonCrawlSegment]:
        compressed_data = requests.get(
            f"{self.data_base_url}/crawl-data/{self.id}/segments/segment.paths.gz"
        ).content

        data = gzip.decompress(compressed_data)
        lines = list(map(str, data.splitlines()))
        segments = []

        for line in lines:
            segments.append(CommonCrawlSegment(
                path=line,
                data_base_url=self.data_base_url
            ))

        return segments