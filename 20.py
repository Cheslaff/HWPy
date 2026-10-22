import re

def task_20(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    pattern = re.compile(r"(?:3[01]|[12][0-9]|0[1-9])\.(?:0[1-9]|1[012])\.\d{4}")
    dates = pattern.findall(text)
    return dates

print(task_20("files/task_20/dates.txt"))