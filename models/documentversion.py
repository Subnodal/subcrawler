from uuid import UUID
from datetime import datetime

class DocumentVersion:
    def __init__(
        self,
        id: UUID,
        url: str,
        normalised_url: str,
        digest: bytes,
        initial_crawl_date: datetime,
        last_crawl_date: datetime
    ):
        self.id = id
        self.url = url
        self.normalised_url = normalised_url
        self.digest = digest
        self.initial_crawl_date = initial_crawl_date
        self.last_crawl_date = last_crawl_date