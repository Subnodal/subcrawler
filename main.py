import argparse

from models.subsearchapi import SubsearchApi
from models.documentsubmitter import DocumentSubmitter
from crawlers.commoncrawl.commoncrawl import CommonCrawl

parser = argparse.ArgumentParser(
    prog="subcrawler",
    description="A flexible and extensible web crawler for Subnodal Search."
)

parser.add_argument(
    "-c", "--crawler",
    help="Which crawler to use."
)

parser.add_argument(
    "-n", "--crawl-count",
    help="Number of resources to crawl.",
    default=1
)

parser.add_argument(
    "-a", "--api-url",
    help="The base URL of the Subsearch API to use when submitting resources.",
    default="http://localhost:8000"
)

args = parser.parse_args()

crawler = None
subsearch_api = SubsearchApi(args.api_url)
document_submitter = DocumentSubmitter(subsearch_api)

match args.crawler:
    case "commoncrawl":
        crawler = CommonCrawl()
    case _:
        raise ValueError("No crawler argument provided")

for _ in range(0, args.crawl_count):
    document = crawler.crawl_next()

    print(document)