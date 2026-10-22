import re
def task_16(path):
    stats = dict()
    error_users = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            status = re.search(r"\b(INFO|WARNING|ERROR)\b", line)
            if status:  # если нашли статсу код
                status = status.group(1)
                stats[status] = stats.get(status, 0) + 1
            else:
                continue

            if status == "ERROR":
                user = re.search(r"\bUser\s+(\d+)", line)
                if user:
                    user_id = user.group(1)
                    error_users.add(user_id)
    return stats, error_users

print(task_16("files/task_16/app.log"))