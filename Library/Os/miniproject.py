import os

path = "D:/Python/Python"

for root, dirs, files in os.walk(path):
    for f in files:
        file_path = os.path.join(root, f)

        if os.path.exists(file_path) and os.path.isfile(file_path):
            size = os.stat(file_path).st_size
            print(file_path, "->", size, "bytes")

input("Press Enter to exit...")
