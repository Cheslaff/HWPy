import time
from contextlib import contextmanager

# 1 способ
class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration = time.perf_counter() - self.start_time
        print(f"Выполнено за: {self.duration:.3f} с.")
        return False


def some_func():
    time.sleep(3)

with Timer():
    some_func()


# 2 способ
@contextmanager
def Timer():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - start_time
        print(f"выполнено за {duration:.3f} с.")

with Timer():
    some_func()