import logging
import sys
import functools

import rich
from rich.console import Console

from chroma.domain.model import OutputFormat

log = logging.getLogger(__file__)

def build_view(output_format):
    if output_format is None:
        output_format = OutputFormat.DEFAULT
    output_format = OutputFormat(output_format)

    match output_format:
        case OutputFormat.TABLE:
            view = Console().print
        case OutputFormat.DEFAULT:
            view = functools.partial(rich.print, file=sys.stdout)
            view.__name__ = f"rich.{rich.print.__name__}"
        case _:
            view = print
    log.debug(f"Built {view.__name__} view")
    return view
