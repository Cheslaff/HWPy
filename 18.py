import re
import json
import logging

def task_18(log_path, out_json):
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")
    # (IP) (call) (URL) (status) 
    pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)\s+(\w+)\s+(\S+)\s+(\d{3})")

    methods = {}
    urls = {}
    errors_4xx = 0

    try:
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                match = pattern.search(line)
                if not match:
                    logging.warning("Пропущена строка: %s", line.strip())
                    continue

                ip, method, url, status = match.groups()
                status = int(status)

                methods[method] = methods.get(method, 0) + 1
                urls[url] = urls.get(url, 0) + 1
                if 400 <= status < 500:
                    errors_4xx += 1

    except FileNotFoundError:
        logging.error("Файл access.log не найден")
        raise

    # самый частый URL
    most_common_url = None
    if urls:
        most_common_url = max(urls, key=urls.get)  # максимум по значению

    stats = {
        "methods": methods,
        "errors_4xx": errors_4xx,
        "most_common_url": most_common_url,
    }

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    logging.info("Завершено: %s", stats)

task_18("files/task_18/access.log", "remake_out/task18.json")