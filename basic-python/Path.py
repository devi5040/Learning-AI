# 1. Using os module
# get current working directory
import os 
print(os.gercwd())

# joining path
path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # Output: folder/subfolder/file.txt (Linux/macOS), folder\subfolder\file.txt (Windows)

# check if file or directory exists
file_path = "example.txt"
if os.path.exists(file_path):
    print("File exists")
else:
    print("File not found")

# check if it's a file or directory
print(os.path.isfile("example.txt"))  # True if it's a file
print(os.path.isdir("my_folder"))    # True if it's a folder

# get file name and directory from a path
file_path = "/home/user/docs/file.txt"
print(os.path.basename(file_path))  # Output: file.txt
print(os.path.dirname(file_path))   # Output: /home/user/docs

# 2. Using pathlib (recommended***)
# create path object 
from pathlib import Path
path = Path("folder") / "subfolder" / "file.txt"
print(path)  # Output: folder/subfolder/file.txt

# get current working directory
print(Path.cwd())  # Returns the current working directory

# get home directory
print(Path.home())  # Returns the home directory of the user

# check if path exists, is it a file or directory
path = Path("example.txt")
print(path.exists())  # True if the file exists
print(path.is_file())  # True if it's a file
print(path.is_dir())   # True if it's a directory

# get file name and parent directory
file_path = Path("/home/user/docs/file.txt")
print(file_path.name)      # Output: file.txt
print(file_path.stem)      # Output: file (without extension)
print(file_path.suffix)    # Output: .txt
print(file_path.parent)    # Output: /home/user/docs

# get absolute path
print(Path("example.txt").resolve())

#3. Creating and Deleting Files/Folders
# creating directory
Path("new_folder").mkdir(exist_ok=True)  # Creates folder, avoids error if it exists

# Remove folder
Path("example.txt").unlink(missing_ok=True)  # Deletes the file

# remove directory