import dataclasses

import pandas as pd
from rich.table import Table

from chroma.domain import model
from chroma.domain.model import OutputFormat


def present_as_table(colour: model.Colour):
    table = Table()
    table.add_column("hex")
    table.add_column("name")
    table.add_column("swatch", style=f"default on {colour.hex}")
    table.add_row(colour.hex, colour.name, "")
    return table


def present_as_html(colour: model.Colour):
    df = pd.DataFrame([dataclasses.asdict(colour)])
    df["swatch"] = ""
    styled = df.style.hide(axis="index").set_properties(
        **{"background-color": colour.hex}, subset=["swatch"]
    )
    return styled.to_html()


def present_as_json(colour: model.Colour):
    return dataclasses.asdict(colour)


def present_asis(colour: model.Colour):
    return colour


def build_presenter(output_format: str | OutputFormat):
    if output_format is None:
        output_format = OutputFormat.DEFAULT
    output_format = OutputFormat(output_format)

    match output_format:
        case OutputFormat.TABLE:
            return present_as_table
        case OutputFormat.JSON:
            return present_as_json
        case OutputFormat.HTML:
            return present_as_html
        case OutputFormat.DEFAULT | _:
            return present_asis
