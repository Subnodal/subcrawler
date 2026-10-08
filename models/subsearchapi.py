import requests
from typing import List, Tuple
from uuid import UUID
from datetime import datetime

from document import Document
from documentversion import DocumentVersion

class SubsearchApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def ingest_documents(self, documents: List[Document]):
        requests.post(self.base_url + "/documents", json={
            "documents": list(map(lambda document: document.serialise(), documents))
        })

    def check_document_versions(self, normalised_urls: List[str]) -> Tuple[List[DocumentVersion], List[str]]:
        response = requests.post(self.base_url + "/document-versions", json={
            "normalised_urls": normalised_urls
        })

        data = response.json()

        document_versions = []
        non_indexed_urls = data["non_indexed"]

        for version_data in data["documents"]:
            document_versions.append(DocumentVersion(
                id=UUID(version_data["id"]),
                url=version_data["url"],
                normalised_url=version_data["normalised_url"],
                digest=bytes.fromhex(version_data["digest"]),
                initial_crawl_date=datetime.fromisoformat(version_data["initial_crawl_date"]),
                last_crawl_date=datetime.fromisoformat(version_data["last_crawl_date"])
            ))

        return document_versions, non_indexed_urls