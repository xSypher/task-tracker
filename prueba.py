with open("tasks.json", "r") as json:
    for i in json.readlines():
        try:
            print(i[2])
        except IndexError:
            pass


        
