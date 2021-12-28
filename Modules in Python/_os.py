# OS MODULE

import os

# create folder
result = os.mkdir("C:/Users/90545/ARTIFICAL INTELLIGENCE/01 - Basics Python/Additional/new_file_10") 

# change folder name
result = os.rename("C:/Users/90545/ARTIFICAL INTELLIGENCE/01 - Basics Python/Additional/new_file_10", "New_File")

# delete empty folder
result = os.rmdir("C:/Users/90545/ARTIFICAL INTELLIGENCE/01 - Basics Python/Additional/new_file_10")

# Listing
result = os.listdir("C:/Users/90545/ARTIFICAL INTELLIGENCE")

# Filtering
for file in os.listdir("C:/Users/90545/ARTIFICAL INTELLIGENCE"):
    if file.endswith("Learning"):
        print(file)

# Get info of defined file or folder
result = os.stat("C:/Users/90545/ARTIFICAL INTELLIGENCE/01 - Basics Python/03 - Functions.ipynb")
print(result)

from datetime import datetime

print("File or folder size is {} KB".format(result.st_size / 1024))
print("File creation date is {}".format(datetime.fromtimestamp(result.st_mtime)))
print("Last access date at file or folder is {}".format(datetime.fromtimestamp(result.st_atime)))
print("Last change date of file or folder is {}".format(datetime.fromtimestamp(result.st_ctime)))

print(os.system("notepad.exe"))  # Open the apps.

result = os.path.exists("C:/can_gülmez/ARAÇLAR/kütüphaneler.txt")
result = os.path.join("C:\\", "Folder_1")
result = os.mkdir(os.path.join("C:\\", "Folder_1"))
result = os.path.split("C:\\Folder_1")
result = os.path.splitext("Introduction to Python.ipynb")

print(result)