import re

def task_23(text):
    return re.sub("\s+", " ", text).strip()

print(task_23("  Hello     world   ! "))