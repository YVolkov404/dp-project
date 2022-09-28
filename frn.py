# for ITEA Programming Basics Course
# diploma project
# created by Yuriy Volkov
# os ---> https://docs.python.org/3/library/os.html
# pathlib ---> https://stackabuse.com/python-list-files-in-a-directory/

import os
import pathlib

# default path as working dir
path = os.path.realpath('./')
work_folder = pathlib.Path(path)


def menu():
    global work_folder

    cli_header = """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # welcome to small python CLI application to rename files
                              ------------------------------
                             diploma project  by yuriy volkov
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    =========================================================
      you can use next commands:
      
        cwd    >_ current working directory
        -.-------------------------------------------------.-
        ls     >_ list files that the folder contains
        -.-------------------------------------------------.-
        cd     >_ change current directory 
        -.-------------------------------------------------.-
        rnm    >_ command to rename file 
           for e.g:
               -> rnm <old_file_name.ext> <new_file_name.ext>
        -.-------------------------------------------------.-
        Y/n    >_ same like yes or no
        -.-------------------------------------------------.-
        q      >_ same like quit or exit
    =========================================================
"""

    print(cli_header)
    input = ""

    while (input != "q"):
        input = get_input()

        if input == "cwd":
            print(" ")
            print_dir()

        if input == "ls":
            for filename in work_folder.iterdir():
                print(" ")
                print(filename)

        if input[0:3] == "rnm":
            arr = input.split(" ")

            if (not arr[1]) or (not arr[2]):
                print(" ")
                print("._error! invalid input")
                continue
            else:
                if arr[1] and arr[2] and os.path.isfile(arr[1]):
                    print(" ")
                    print(">_ you're gonna rename: " +
                          arr[1] + " to " + arr[2])
                    print(" ")
                    print(">_ it will impact the next file: ")
                    print(" ")
                    for filename in work_folder.iterdir():
                        if arr[1] in str(filename):
                            print(filename)
                    print(" ")
                    print(">_ do you want to continue? [Y/n]")
                    check_out = get_input()
                    if (check_out == "n"):
                        print(" ")
                        print("._renaming cancelled!")
                        continue
                    if (check_out == "Y") or (check_out == "y"):
                        full_rename(arr[1], arr[2])
                        print(" ")
                        print("._filename changed:")
                        print(" ")
                        for filename in work_folder.iterdir():
                            if arr[2] in str(filename):
                                next_name = arr[2]
                                print(next_name)
                else:
                    print(" ")
                    print("._filename wasn't found!")
                    get_input()

        if input[0:2] == "cd":
            print(" ")
            temp_folder = work_folder

            if input[3:5] == "..":
                new_path = work_folder.parent
                work_folder = pathlib.Path(new_path)
            else:
                new_path = os.path.join(work_folder, input[3:])
                work_folder = pathlib.Path(new_path)

            print_dir()

        if not os.path.isdir(work_folder):
            print(" ")
            print("._wrong folder!")
            work_folder = temp_folder


def print_dir():
    print(str(work_folder))


def get_input():
    print("")
    return input(">_ use the command: ")


def full_rename(filename1, filename2):
    last_name = filename1
    next_name = filename2
    os.rename(last_name, next_name)


menu()