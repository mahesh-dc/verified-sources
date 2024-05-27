# generated by datamodel-codegen:
#   filename:  catalog.yml
#   timestamp: 2024-05-27T08:56:40+00:00

from __future__ import annotations

from typing import List, Union, Literal
from pydantic import Field

from dat_core.pydantic_models import DatDocumentStream, DatCatalog


class TxtDatStream(DatDocumentStream):
    name: str = Literal['txt']
    dir_prefix: str


class PdfDatStream(DatDocumentStream):
    name: str = Literal['pdf']
    dir_prefix: str


class AmazonS3Catalog(DatCatalog):
    document_streams: List[Union[TxtDatStream, PdfDatStream]]
