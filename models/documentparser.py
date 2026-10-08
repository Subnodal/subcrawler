from abc import ABC, abstractmethod

from models.document import Document

class DocumentParser(ABC):
    @abstractmethod
    def parse(self, data) -> Document:
        pass