from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        reader = csv.DictReader(file)

        return [dict(row) for row in reader]
# list
# List of rows as dicts


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    lista_job_type = [row["job_type"] for row in data]
    return set(lista_job_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    raise NotImplementedError
