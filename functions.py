from datetime import date
TODAY = date.today().__str__()

def get_ids(json_file) -> list:
    ids = []
    with open(json_file, 'r') as json:
        for line in json.readlines():
            try:
                ids.append(line[2])
            except IndexError:
                pass
    return ids

def add(args: list, id: int, json_file):
    id += 1
    #check if a description exists and whether it's an integer.
    try:
        argument = int(args[1])
        raise ValueError(f"ERROR: Invalid argument: {argument}")
    
    except IndexError:
        raise IndexError("ERROR: Description is missing.")
    
    except ValueError:
        with open(json_file, "r") as json:
            task = {"description": args[1], "status": "Todo", "createdAt": TODAY, "updatedAt": "None"}
            lines = json.readlines()
            lines[len(lines)-1] = f'\t"{id}": {task},\n'
            lines.append('}')
        with open(json_file, "w") as json:
            json.writelines(lines)
        return f"Task added succesfully (ID: {id})"