from contextlib import contextmanager

@contextmanager
def log_operation(filename, operation):
    with open(filename, "a", encoding="utf-8") as lf:
        lf.write(f"START: {operation}\n")
        try:
            yield
        except Exception:
            lf.write(f"ERROR: {operation}\n")
            raise
        else:
            lf.write(f"END {operation}\n")

with log_operation("output/task_14/operation.log", "data cleaning"):
    print("Cleaning data")