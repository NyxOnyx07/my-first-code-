import os

# Select the directory whose contnt you want to list
directory_path = '/'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the conntents of the directory
print(contents)