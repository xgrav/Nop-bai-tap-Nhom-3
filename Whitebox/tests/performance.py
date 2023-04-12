from memory_profiler import profile, memory_usage
from src.source import is_prime
import random
import timeit

@profile
def randomprime():
    is_prime(
        random.randrange(-100, 100)
    )
if __name__ == "__main__":
    execution_time = timeit.timeit(randomprime, number=1)
    print(f"Execution time: {execution_time}")