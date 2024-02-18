import textwrap
import os

import pytest

from chroma import main


@pytest.fixture
def dummy_data_source(tmp_path):
    data = tmp_path / "dummy.csv"
    data.write_text(
        textwrap.dedent(
            """\
            hex,name
            #FFFFFF,white
            """
        )
    )
    return data


@pytest.fixture
def sandbox_env(dummy_data_source):
    os.environ["DATA_SOURCE"] = "CSV"
    os.environ["DATA_URI"] = str(dummy_data_source)


def test_name(sandbox_env, capsys):
    main.name(output_format="json", seed=0)
    capsys.readouterr().out.startswith('{"hex": "#FFFFFF", "name": "white"}')
