from io import StringIO

def count_lines(stream):
    return sum(1 for line in stream)

with open("files/task_15/data.txt", "r", encoding="utf-8") as f:
    print(count_lines(f))  # подсчёт в файле

# подсчёт из потока
print(count_lines(StringIO("first\nsecond\nthird")))