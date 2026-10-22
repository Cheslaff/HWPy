import re

def task_11(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    errors = re.findall(r"^ERROR.*$", text, flags=re.MULTILINE)
    ids = re.findall(r"User\s+(\d+)\s+", text)
    error_ids = re.findall(r"^ERROR\s+User\s+(\d+)", text, flags=re.MULTILINE)
    print(errors, ids, error_ids)

task_11("files/task_11/logs.txt")