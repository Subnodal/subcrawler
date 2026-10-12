from typing import Optional
from abc import ABC, abstractmethod

from models.document import Document

class Crawler(ABC):
    @abstractmethod
    def crawl_next(self) -> Optional[Document]:
        pass