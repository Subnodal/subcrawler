from typing import List

from document import Document
from subsearchapi import SubsearchApi

class DocumentSubmitter:
    def __init__(self, subsearch_api: SubsearchApi):
        self.subsearch_api = subsearch_api

        self.queue: List[Document] = []

    def add_to_queue(self, document: Document):
        self.queue.append(document)

    def remove_already_indexed(self):
        document_versions, _ = self.subsearch_api.check_document_versions(
            list(map(lambda document: document.normalised_url, self.queue))
        )

        already_indexed_digests = []
        remaining_documents = []

        for document_version in document_versions:
            digest = document_version.digest

            if digest is None:
                continue

            already_indexed_digests.append(digest)

        for document in self.queue:
            if document.digest in already_indexed_digests:
                continue

            remaining_documents.append(document)

        self.queue = remaining_documents

    def submit_all(self):
        self.subsearch_api.ingest_documents(self.queue)

        self.queue = []