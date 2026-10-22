import csv

def task_4(input_path, output_path):
    records = []
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for record in reader:
            if float(record["price"]) > 100:
                records.append(record)

    with open(output_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

task_4("files/task_04/products.csv", "remake_out/task4.csv")