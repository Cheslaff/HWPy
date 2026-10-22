import re
def task_22(text):
    return re.findall(r"(?:https?://)[^\s,]+", text)

text = "http://page.html is not safe, use https://google.com"
print(task_22(text))