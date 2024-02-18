import sys

import rich
from rich.console import Console

from chroma.domain.model import OutputFormat


def build_view(output_format):
    if output_format is None:
        output_format = OutputFormat.DEFAULT
    output_format = OutputFormat(output_format)

    match output_format:
        case OutputFormat.TABLE:
            view = Console().print
        case OutputFormat.DEFAULT:
            view = lambda x: rich.print(x, file=sys.stdout)
        case _:
            view = print
    return view
