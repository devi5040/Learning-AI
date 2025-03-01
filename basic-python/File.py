# modes => r->read, w->write(overwrite), a->append, x->create a new file, b->binary mode, t->text mode
# 1. open() method
# file = open(filename,mode)

# 2. Reading a file using read() method to read entire file
file = open('filename','r')
content = file.read()
print(content)
file.close()

# 3. using readline() to read line by line
file = open('filename','r')
print(file.readline())
file.close()

# 4. using readlines() to read all lines as a list
file = open('filename','r')
lines = file.readlines()
print(lines)
file.close()

# 5. write() overwrites the existing file
file = open('sample.txt','w')
file.write('Hello first line')
file.close()

# 6. writelines() writes many lines
lines = ['line1','line2','line3']
file = open('sample.txt','w')
file.writelines(lines)
file.close()

# 7. Appending to a file 
file = open("sample.txt", "a")
file.write("This is an appended line.\n")
file.close()

# 8. Using with (using with alongside open() will automatically closes the file)
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)  # File closes automatically after this block

# 9. Checking if a file exists using os
import os
if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")

# 10. Deleting a file
import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted")
else:
    print("File not found")

# 11. Working with pathlib
from pathlib import Path
file_path = Path("sample.txt")
if file_path.exists():
    print("File exists at:", file_path.resolve())  # Get absolute path

# 12. Reading and Writing binary files
with open("image.jpg", "rb") as img:
    content = img.read()

with open("image.jpg", "rb") as source:
    with open("copy.jpg", "wb") as destination:
        destination.write(source.read())

# 13. Working with json file
import json
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Output: {'name': 'Alice', 'age': 25}
