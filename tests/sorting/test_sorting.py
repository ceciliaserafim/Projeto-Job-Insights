from src.pre_built.sorting import sort_by


jobs = [
    {'max_salary': '3812', 'min_salary': '1984', 'date_posted': '2020-05-02'},
    {'max_salary': '4000', 'min_salary': '1000', 'date_posted': '2021-05-02'},
    {'max_salary': '5000', 'min_salary': '2000', 'date_posted': '2022-05-02'},
    ]

job_max_salary = [
    {'max_salary': '5000', 'min_salary': '2000', 'date_posted': '2022-05-02'},
    {'max_salary': '4000', 'min_salary': '1000', 'date_posted': '2021-05-02'},
    {'max_salary': '3812', 'min_salary': '1984', 'date_posted': '2020-05-02'},
    ]

job_min_salary = [
    {'max_salary': '4000', 'min_salary': '1000', 'date_posted': '2021-05-02'},
    {'max_salary': '3812', 'min_salary': '1984', 'date_posted': '2020-05-02'},
    {'max_salary': '5000', 'min_salary': '2000', 'date_posted': '2022-05-02'},
    ]

job_date_posted = [
    {'max_salary': '5000', 'min_salary': '2000', 'date_posted': '2022-05-02'},
    {'max_salary': '4000', 'min_salary': '1000', 'date_posted': '2021-05-02'},
    {'max_salary': '3812', 'min_salary': '1984', 'date_posted': '2020-05-02'},
    ]


def test_sort_by_criteria():   
    sort_by(jobs, 'max_salary')
    assert jobs == job_max_salary
    
    sort_by(jobs, 'min_salary')
    assert jobs == job_min_salary

    sort_by(jobs, 'date_posted')
    assert jobs == job_date_posted