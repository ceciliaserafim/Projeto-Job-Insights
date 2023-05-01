from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    lista_industry = [row["industry"] for row in data]
    lista_industry = filter(None, lista_industry)
    return set(lista_industry)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [all_jobs for all_jobs in jobs
            if all_jobs["industry"] == industry]
