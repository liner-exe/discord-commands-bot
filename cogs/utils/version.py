def get():
    with open("version.txt", "r", encoding="utf-8") as file:
        return file.read()