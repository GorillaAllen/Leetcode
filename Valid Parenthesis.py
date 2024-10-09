s = "()[]{"
while True:
    length = len(s)
    if r"()" in s:
        s = s.replace("()","")
    if r"[]" in s:
        s = s.replace("[]","")
    if r"{}" in s:
        s = s.replace("{}","")
    if length == len(s) and len(s) != 0:
        print(False)
        break
    if s == "":
        print(True)
        break
        