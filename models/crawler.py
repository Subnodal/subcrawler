from abc import ABC, abstractmethod

from documentsubmitter import DocumentSubmitter

class Crawler(ABC):
    @abstractmethod
    def crawl(self, document_submitter: DocumentSubmitter):
        pass