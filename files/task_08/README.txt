Suggested paths:
- existing.txt -> successful read
- missing.txt -> FileNotFoundError (the file is intentionally absent)
- no_access.txt -> PermissionError on Unix if permissions are preserved; otherwise run chmod 000 no_access.txt
- directory_instead_of_file -> IsADirectoryError / another OSError depending on code
