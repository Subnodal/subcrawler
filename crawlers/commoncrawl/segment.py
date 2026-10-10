import requests
import gzip
from typing import List

from crawlers.commoncrawl.archive import CommonCrawlArchive

class CommonCrawlSegment:
    def __init__(
            self,
            path: str,
            data_base_url: str
        ):
        self.path = path
        self.data_base_url = data_base_url

    def get_archives(self) -> List[CommonCrawlArchive]:
        compressed_data = requests.get(
            f"{self.data_base_url}/{self.path}warc.paths.gz"
        ).content

        data = gzip.decompress(compressed_data)
        lines = list(map(str, data.splitlines()))
        archives = []

        for line in lines:
            archives.append(CommonCrawlArchive(
                path=line,
                data_base_url=self.data_base_url
            ))

        return archives