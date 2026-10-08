import enum
from typing import Optional
from datetime import datetime
from ipaddress import IPv4Address, IPv6Address

class DatePrecision(enum.Enum):
    DAY = 1
    SECOND = 2
    MILLISECOND = 3

    @staticmethod
    def from_str(value):
        return {
            "day": DatePrecision.DAY,
            "second": DatePrecision.SECOND,
            "millisecond": DatePrecision.MILLISECOND
        }[value]

    @staticmethod
    def to_str(value):
        return {
            DatePrecision.DAY: "day",
            DatePrecision.SECOND: "second",
            DatePrecision.MILLISECOND: "millisecond"
        }[value]

class Document:
    def __init__(
        self,
        url: str,
        digest: Optional[bytes],
        title: str,
        description: Optional[str],
        body: str,
        lang: Optional[str],
        source_ip_addr: Optional[IPv4Address | IPv6Address],
        publication_date: Optional[datetime],
        publication_date_precision: Optional[DatePrecision],
        has_consent_or_pay_model: bool,
        has_advertisements: bool,
        has_paywall: bool,
        has_login_wall: bool,
        has_generative_ai_content: bool
    ):
        if publication_date is not None and publication_date_precision is None:
            raise ValueError("Publication date provided without precision")

        if publication_date is None and publication_date_precision is not None:
            raise ValueError("Publication date precision provided without date")

        self.url = url
        self.digest = digest

        self.title = title
        self.description = description
        self.body = body

        self.lang = lang
        self.source_ip_addr = source_ip_addr

        self.publication_date = publication_date
        self.publication_date_precision = publication_date_precision

        self.has_consent_or_pay_model = has_consent_or_pay_model
        self.has_advertisements = has_advertisements
        self.has_paywall = has_paywall
        self.has_login_wall = has_login_wall
        self.has_generative_ai_content = has_generative_ai_content

    @property
    def normalised_url(self) -> str:
        return self.url

    @property
    def ip_region(self) -> Optional[str]:
        return None

    def serialise(self):
        return {
            "url": self.url,
            "normalised_url": self.normalised_url,
            "digest": self.digest,
            "title": self.title,
            "description": self.description,
            "body": self.body,
            "lang": self.lang,
            "ip_region": self.ip_region,
            "publication_date": (
                self.publication_date.isoformat()
                if self.publication_date is not None
                else None
            ),
            "publication_date_precision": (
                DatePrecision.to_str(self.publication_date_precision)
                if self.publication_date_precision is not None
                else None
            ),
            "has_consent_or_pay_model": self.has_consent_or_pay_model,
            "has_advertisements": self.has_advertisements,
            "has_paywall": self.has_paywall,
            "has_login_wall": self.has_login_wall,
            "has_generative_ai_content": self.has_generative_ai_content
        }