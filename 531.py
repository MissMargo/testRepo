import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

    for file in files("."):
        print(file)
    #directory = r"/Users/margo/PycharmProjects"
    #list = os.walk(directory)
    number_files = len(list)
    #print(number_files)


    #print(catalogs)

# print(os.listdir(path="/Users/margo"), "\n")
# print(os.path.basename("r/Users/margo/PycharmProjects/pythonProject/dict.txt"))
