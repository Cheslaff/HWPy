def task_1(path):
    n_rows = 0
    n_words = 0
    n_chars = 0
    max_len = 0
    with open(path, "r", encoding="utf-8") as f:
        for row in f:
            n_rows += 1
            n_words += len(row.split())
            n_chars += len(row)
            max_len = max(max_len, len(row.rstrip("\n")))

    return n_rows, n_words, n_chars, max_len

files = ["empty.txt", "single_line.txt", "text.txt"]

for file in files:
    n_rows, n_words, n_chars, max_len = task_1(f"files/task_01/{file}")
    print(f"File: {file}")
    print(f"n_rows: {n_rows} | n_words: {n_words}")
    print(f"n_chars: {n_chars} | max_len: {max_len}")
    print("---")