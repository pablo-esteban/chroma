import csv
import pathlib
import sqlite3

from chroma import config
from chroma.domain import model


class CsvFileRepository:
    def __init__(self, path: str | pathlib.Path):
        with open(path) as file_handle:
            reader = csv.DictReader(file_handle)
            self._data = [model.Colour(**row) for row in reader]

    def get(self) -> list[model.Colour]:
        return self._data


class SqliteRepository:
    def __init__(self, connection):
        self._connection = connection

    def get(self) -> list[model.Colour]:
        self._connection.row_factory = sqlite3.Row
        data = self._connection.execute("SELECT * FROM colours").fetchall()
        self._connection.close()
        colours = [model.Colour(*row) for row in data]
        return colours


def get_repository(data_source_type):
    match data_source_type:
        case 'CSV':
            return CsvFileRepository(config.get_data_uri())
        case 'DB_SQLITE':
            return SqliteRepository(sqlite3.connect(config.get_data_uri()))
        case _:
            raise ValueError(f"Unknown data source type {data_source_type=}")