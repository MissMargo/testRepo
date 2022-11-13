import os
for dirs, files in os.walk(r"/Users/margo/PycharmProjects"):
    for _dir in dirs:
        print(_dir)

    for _file in files:
        print(_file)
