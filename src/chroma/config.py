import os
import logging

log = logging.getLogger(__file__)


def get_data_uri():
    data_uri = os.environ.get("DATA_URI", "file:data/essential.csv")
    log.debug(f"{data_uri=}")
    return data_uri


def get_datasource_type():
    datasource_type = os.environ.get("DATA_SOURCE", "CSV")
    log.debug(f"{datasource_type=}")
    return datasource_type
