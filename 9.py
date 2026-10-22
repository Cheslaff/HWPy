import re

def parse_number(value):
    match = re.fullmatch(r"-?\d+(?:\.\d+)?", value)
    if match:
        return float(value)
    else:
        raise ValueError("Некорректное значение")

print(parse_number("-23.056"))