def task_17(path):
    sum_ = 0
    min_ = float("inf")
    max_ = float("-inf")
    n_nums = 0

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                num = int(line)
                sum_ += num
                min_ = min(min_, num)
                max_ = max(max_, num)
                n_nums += 1
            except ValueError:
                continue
        if n_nums > 0: mean = sum_ / n_nums
        else: mean = 0
    return sum_, min_, max_, n_nums, mean

print(task_17("files/task_17/big_numbers.txt"))