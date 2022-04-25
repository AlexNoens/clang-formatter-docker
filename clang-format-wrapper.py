#!/usr/bin/env python3

import os
import time


def get_c_files():
    c_extensions = (
        ".c",
        ".h",
        ".C",
        ".H",
        ".cpp",
        ".hpp",
        ".cc",
        ".hh",
        ".c++",
        ".h++",
        ".cxx",
        ".hxx",
    )
    files = os.listdir(".")
    c_files = []
    sub_dirs = []
    while 1:
        for each in files:
            if os.path.isdir(each):
                for sub_folder in os.listdir(each):
                    sub_dirs.append(os.path.join(each, sub_folder))
            else:
                if each.endswith(c_extensions):
                    c_files.append(each)
        if len(sub_dirs) != 0:
            files = sub_dirs.copy()
            sub_dirs = []
        else:
            break
    return " ".join(c_files)


def main():
    format_command = "clang-format -i " + get_c_files()
    os.system(format_command)


if __name__ == "__main__":
    main()
