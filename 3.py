import csv

def task_3(path):
    top_score = float("-inf")
    top_student = None
    scores_sum = 0
    n_students = 0
    group_sum = dict()
    global_mean = 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for record in reader:
            name = record["name"]
            group = int(record["group"])
            score = float(record["score"])

            if score > top_score:
                top_score = score
                top_student = name
                
            if group not in group_sum:
                group_sum[group] = []
            group_sum[group].append(score)
            scores_sum += score
            n_students += 1

    if n_students > 0:
        global_mean = scores_sum / n_students
    
    print(f"Student: {top_student} Score:{top_score}")
    print(f"Global mean: {global_mean}")
    print("Group_mean", {group: sum(scores) / len(scores) for group, scores in group_sum.items()})

task_3("files/task_03/students.csv")