import csv
from typing import Iterable, Callable
def my_filter(it: Iterable, predicate: Callable[[any], bool]) -> Iterable:
    return [i for i in it if predicate(i)]
def my_count(it: Iterable) -> int:
    count = 0
    return [count := count + 1 for _ in it][-1]
with open('StudentsPerformance 14.csv', 'r') as f:
    reader = csv.DictReader(f)
    students = [s for s in reader]
    lunched_score = my_filter(students, lambda s: s['writing score'] == '>90' and s['lunch'] == 'standard')
    print(my_count(lunched_score))
    pass