from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    salary = [
        int(row["max_salary"])
        for row in data if row["max_salary"].isdigit()]
    return max(salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    salary_min = [
        int(row["min_salary"])
        for row in data if row["min_salary"].isdigit()]
    return min(salary_min)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary = int(salary)
    except (ValueError, TypeError, KeyError):
        raise ValueError(
            'As chaves min_salary e max_salary devem ser numericas'
        )
    if min_salary > max_salary:
        raise ValueError(
            'O valor de min_salary não pode ser maior que max_salary'
            )
    return min_salary <= salary <= max_salary


def filter_by_salary_range(
        jobs: List[dict], salary: Union[str, int]
        ) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
