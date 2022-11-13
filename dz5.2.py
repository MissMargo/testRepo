def new_dict():
    with open('dict.txt') as file:
        lines = file.read().splitlines()

    dic = {}

    for line in lines:
        key, value = line.split(': ')
        dic.update({key: value})

    print(dic)


new_dict()
