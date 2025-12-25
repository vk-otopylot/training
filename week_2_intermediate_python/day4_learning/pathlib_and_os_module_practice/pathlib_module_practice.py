# Create Folder & File Using Pathlib

from pathlib import Path
#
# folder_name = input('Enter the folder name: ')
#
# p = Path(folder_name)
# file_path = p / 'log.txt'
#
# try:
#     p.mkdir()
#     file_path.touch()
#
#     with (p / 'log.txt').open('w') as file:
#         file.write("Project initialized")
#
# except FileExistsError as f:
#     print(f)
#
# except PermissionError as p:
#     print(p)


# Check If File Exists & Show File Details

# file_path = input('Enter the file path: ')
# p = Path(file_path)
# try:
#     if not p.exists():
#         raise FileNotFoundError
#     print(p.name)
#     print(p.parent)
#     print(p.suffix)
#     if p.exists():
#         st_file = p.stat()
#         print(st_file.st_size)
#
# except FileNotFoundError as f:
#     print("Error: File does not exist.")


# Rename File Using Pathlib

# file_path = input('Enter the file path: ')
# path = Path(file_path)
# try:
#     if not path.exists():
#         raise FileNotFoundError
#     n_name = input('Enter New File Name: ')
#     n_path = path.parent / n_name
#     path.rename(n_path)
#
# except FileNotFoundError:
#     print("Error: File does not exist.")
#
# except FileExistsError:
#     print("Error: File already exist.")
#
# except PermissionError:
#     print('Error: You do not have permission to change filename.')


# Delete File Safely

file_path = input('Enter the file path: ')
path = Path(file_path)

try:
    if not path.exists():
        raise FileNotFoundError
    confirm = input(f'Are you sure to delete {path.name} (yes/no): ')
    if confirm == 'yes':
        path.unlink()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print('Error: You do not have permission delete file.')