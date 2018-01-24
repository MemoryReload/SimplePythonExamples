import os

def index(dir):
    files = []
    dir_stack = [dir]

    while dir_stack:
        cudir = dir_stack.pop()
        for file in os.listdir(cudir):
            file_abs = os.path.join(cudir,file)
            if os.path.isdir(file_abs):
                dir_stack.append(file_abs)
            elif os.path.isfile(file_abs) and not os.path.islink(file_abs):
                files.append(file_abs)
            else:
                file
