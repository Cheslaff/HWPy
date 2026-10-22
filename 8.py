def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Файла не существет!")
    except PermissionError:
        print("Нет прав доступа!")
    except UnicodeDecodeError:
        print("Ошибка чтения файла!")
    except IsADirectoryError:
        print("Предоставленный путь - директория")
    except OSError:
        print("Ошибка OS")