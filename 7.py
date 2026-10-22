from pathlib import Path

def task_7(dir_path, suffix):
    root = Path(dir_path)
    if not root.exists() or not root.is_dir():
        print("Ошибочка")
        return
    for obj in root.rglob(f"*{suffix}"):
        print(obj, obj.stat().st_size)

task_7("files/task_07/project", ".py")