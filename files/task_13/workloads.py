import time

def fast_work():
    return sum(range(10_000))

def slow_work():
    time.sleep(0.05)
    return "done"

def failing_work():
    time.sleep(0.01)
    raise RuntimeError("test error")
