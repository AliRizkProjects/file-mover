'''
This program is mainly for my personal use to organize my files more quickly, without
having to navigate through folders manually or create shortcuts.
Paths can be customized to suit individual preferences.
'''

import shutil
import os
import sys
import getpass

username = getpass.getuser()

# Semester specification, in case folders are divided by semester.
semester = input("Enter the semester (as a number) to which the file belongs: ") + ". Semester"

start_path = os.path.join('/Users', username, 'OneDrive', 'Uni', 'FU', semester)

def check_file(filename):
    modules = ["ALP3", "ALP4", "TI2", "TI3", "Statistics", "Statistics_II"]

    # The list is reversed to prioritize the recognition of exercise numbers with two digits (e.g., 12, 13) first.
    exercises = reversed([f"U{i}" for i in range(1, 15)])

    # If module name and exercise number are present in the filename, search for the file
    matches = [(mod, ex) for mod in modules for ex in exercises if mod in filename and ex in filename]

    if matches:
        module = matches[0][0]
        exercise = matches[0][1]
        target_path = os.path.join(start_path, module, exercise)
        if os.path.exists(target_path):
            move_file(filename, target_path)
        else:
            check_path(filename, target_path)
    else:
        print("File not found.")

def check_path(file, pathToCheck):
    path_parts = pathToCheck.split(os.path.sep)
    for i in range(1, len(path_parts) + 1):
        sub_path = os.path.join(*path_parts[:i])
        if not os.path.exists(sub_path):
            create_folder = input(f"The folder '{sub_path}' does not exist.\nShould this folder be created? (Y/N): ")
            if create_folder.lower() == 'y':
                os.makedirs(sub_path)
                check_file(file)
            else:
                print("Process canceled, folder will not be created.")
                break

def move_file(filename, destination):
    current_directory = os.path.dirname(filename)
    files = os.listdir(current_directory)
    baseName = os.path.splitext(os.path.basename(filename))[0]
    
    # Move all files with the correct filename (exercise name + number)
    found_files = [file for file in files if baseName in os.path.splitext(file)[0]]
    print(found_files)
    if found_files:
        print(f"Found files matching the criteria: {found_files}")
        for file in found_files:
            moveFile = input(f"File {file} will be moved to {destination}.\nContinue? (Y/N): ")
            if moveFile.lower() == 'y':
                source = os.path.join(current_directory, file)
                shutil.move(source, destination)
    else:
        print(f"No file(s) with this name in directory {current_directory} found")

if len(sys.argv) != 2:
    print("Please provide exactly one filename")
else:
    argument = sys.argv[1]
    check_file(argument)
