import json

def task_5(input_path, output_path):
    max_score = 0
    max_score_student = None
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for student in data:
            student["passed"] = bool(student["score"] >= 60)
            if student["score"] > max_score:
                max_score = student["score"]
                max_score_student = student["name"]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"{max_score_student} : {max_score}")

task_5("files/task_05/students.json", "remake_out/task5.json")