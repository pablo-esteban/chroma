import dataclasses
import enum


@dataclasses.dataclass
class Colour:
    hex: str
    name: str


class OutputFormat(enum.Enum):
    DEFAULT = "default"
    HTML = "html"
    TABLE = "table"
    JSON = "json"
