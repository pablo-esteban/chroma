import os


def get_data_uri():
    return os.environ.get("DATA_URI", "file:data/essential.csv")


def get_datasource_type():
    return os.environ.get("DATA_SOURCE", "CSV")
