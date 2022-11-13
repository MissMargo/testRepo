def create_dict_file():
    dict_1 = {'country': "Ukraine"}
    f = open("dict.txt", "w")
    f.write(str(dict_1))
    f.close()


create_dict_file()




