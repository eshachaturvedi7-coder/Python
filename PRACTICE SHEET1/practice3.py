import os

# Specify the directory path
path = '/New folder'   # Replace with your directory path

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)