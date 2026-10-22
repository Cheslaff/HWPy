import re

def task_12(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return list(dict.fromkeys(emails))

print(task_12("files/task_12/text.txt"))