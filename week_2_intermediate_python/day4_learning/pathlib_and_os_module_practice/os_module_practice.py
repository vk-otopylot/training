import os

# Create Folder Using OS Module

# folder_name = input('Enter the folder name: ')
#
# try:
#     os.mkdir(folder_name)
#     print('Folder creates successfully.')
# except FileExistsError:
#     print('Error: File Already Exists')
# except PermissionError:
#     print('Error: You do not have permission to create folder.')

# Rename File Using OS Module

# os.chdir('kuldeep')
#
# old_name = input('Enter old file name: ')
# new_name = input('Enter new file name: ')
#
# try:
#     if not os.path.exists(old_name):
#         raise FileNotFoundError
#     parent_dir = os.path.dirname(old_name)
#     new_path = os.path.join(parent_dir, new_name)
#
#     os.rename(old_name, new_path)
#
# except FileNotFoundError:
#     print('Error: File does not Exists.')
#
# except PermissionError:
#     print('Error: You do not have permission to rename file.')


# Find All .txt Files in a Folder

root_folder = input('Give me root folder path: ')

try:
    if not os.path.exists(root_folder):
        raise FileNotFoundError
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.txt'):
                full_path = os.path.join(root, file)
                print(full_path)

except FileNotFoundError:
    print('Error: File does not exists.')