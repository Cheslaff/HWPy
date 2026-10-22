def task_2(input_path, output_path):
    min_val = float("inf")
    max_val = float("-inf")
    sum_ = 0
    n_rows = 0

    # Считываем статистики из файла
    with open(input_path, "r", encoding="utf-8") as f:
        for val in f:
            try:
                val = int(val)
                min_val = min(min_val, val)
                max_val = max(max_val, val)
                sum_ += val
                n_rows += 1
            except ValueError:
                pass

    # Загружаем статистику в файл
    with open(output_path, "w", encoding="utf-8") as f:
        if n_rows != 0:
            f.write(f"min: {min_val}\nmax: {max_val}\nmean: {sum_ / n_rows}")
        else:
            f.write("Пустой файл\n")

task_2("files/task_02/numbers_mixed.txt", "remake_out/task2.txt")
