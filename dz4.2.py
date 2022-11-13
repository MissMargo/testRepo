def merged():

    dict_1 = {"id": 1, "name": "Alex"}
    dict_2 = {"Surname": "Ivanenko", "Date of birth": "01/01/2010"}
    dict_3 = {"city": "Lviv", "country": "Ukraine"}
    merged_dict = {**dict_1, **dict_2, **dict_3}
    print(merged_dict)


merged()
