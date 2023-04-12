from memory_profiler import profile, memory_usage
from src.source import check_triangle
import random
import timeit

@profile
def metricchecktriangle():
    check_triangle(
        random.randrange(-100, 100), random.randrange(-100, 100), random.randrange(-100, 100)
    )
if __name__ == "__main__":
    execution_time = timeit.timeit(metricchecktriangle, number=1)
    print(f"Execution time: {execution_time}")