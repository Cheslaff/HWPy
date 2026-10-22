import re

def task_24(products):
    valid = []
    for product in products:
        if re.fullmatch("^PRD-\d{5}$", product):
            valid.append(product)
    return valid

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]
print(task_24(products))