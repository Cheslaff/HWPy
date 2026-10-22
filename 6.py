import pathlib

def task_6(dir_path):
    n_files = 0
    n_subdirs = 0
    python_files = []
    sum_size = 0

    dir_path = pathlib.Path(dir_path)
    for object in dir_path.rglob("*"):
        if object.is_file():
            n_files += 1
            sum_size += object.stat().st_size
            if object.suffix == ".py":
                python_files.append(object.name)
        elif object.is_dir():
            n_subdirs += 1
        
    print(n_files, n_subdirs, python_files, sum_size)

task_6("files/task_06/catalog")