from abc import ABC, abstractmethod

from documentsubmitter import DocumentSubmitter

class Crawler(ABC):
    @abstractmethod
    def crawl_next(self, document_submitter: DocumentSubmitter):
        pass