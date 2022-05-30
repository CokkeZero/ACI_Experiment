import os


def getFiles(folder):
    files = [];

    path_of_the_directory = folder
    ext = ('.txt')
    for file in os.listdir(path_of_the_directory):
        if file.endswith(ext):
            files.append(file)
        else:
            continue

    print(files)
    return(files)