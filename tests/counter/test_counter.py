from src.pre_built.counter import count_ocurrences

# testa quantas vezes a palavra word aparece


def test_counter():
    path = "data/jobs.csv"
    word = "python"

    assert count_ocurrences(path, word) == 1639

    word = "PYTHON"
    assert count_ocurrences(path, word) == 1639
