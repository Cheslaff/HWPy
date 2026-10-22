import re

def task_19(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    phones = re.findall(r"(?:\+7|8) (?:\(\d{3}\)|\d{3}) \d{3}-\d{2}-\d{2}", text)
    return phones

print(task_19("files/task_19/phones.txt"))