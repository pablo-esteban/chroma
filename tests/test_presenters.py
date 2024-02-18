from unittest import mock

import pytest
from rich.table import Table

from chroma.domain import model
from chroma.ui import presenters


@pytest.fixture
def given():
    return model.Colour("#FFFFFF", "white")


def test_present_asis(given):
    expected = given
    observed = presenters.present_asis(given)
    assert observed == expected


def test_present_as_json(given):
    observed = presenters.present_as_json(given)
    expected = {"hex": "#FFFFFF", "name": "white"}
    assert observed == expected


def test_present_as_table(given):
    observed = presenters.present_as_table(given)
    assert isinstance(observed, Table)


def test_present_as_html(given):
    observed = presenters.present_as_html(given)
    assert "<table" in observed
    assert "</table>" in observed
