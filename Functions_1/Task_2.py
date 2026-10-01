import os

def list_folder(folder_name):
    if not os.path.isdir(folder_name):
        print("Error: folder not found.")
        return

    try:
        files = os.listdir(folder_name)
    except PermissionError:
        print("Error: permission denied.")
        return

    print(f"Files in {folder_name}:")
    for name in files:
        print(f"  {name}")

def rename_file(old_name, new_name):
    if not os.path.isfile(old_name):
        print("Error: file not found.")
        return

    if os.path.exists(new_name):
        print("Error: new file name already exists.")
        return

    try:
        os.rename(old_name, new_name)
    except PermissionError:
        print("Error: permission denied.")
        return

    print(f"Updated file name: {new_name}")

if __name__ == "__main__":
    list_folder(".")
    list_folder("no_such_folder")

    with open("old_name.txt", "w") as f:
        f.write("test")

    rename_file("old_name.txt", "new_name.txt")
    rename_file("old_name.txt", "new_name.txt")

    os.remove("new_name.txt")