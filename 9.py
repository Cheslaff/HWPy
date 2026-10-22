import re

def parse_number(value):
    match = re.fullmatch(r"-?\d+(?:\.\d+)?", value)
    if match:
        return float(value)
    else:
        raise ValueError("Некорректное значение")

try:
    print(parse_number(input("Enter a number: ")))
except ValueError as e:
    print(f"Неправильный ввод: {e}")
