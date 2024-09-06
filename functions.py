from datetime import date
TODAY = date.today().__str__()
JSON_FILE = "tasks.json"



#get the ids fo the existing tasks
def get_ids() -> list:
    ids = []
    with open(JSON_FILE, 'r') as json:
        for line in json.readlines():
            try:
                if line[3] + line[4] == "ID":
                    ids.append(line[9])
            except IndexError:
                pass
    return ids

def add(args: list, id: int):

    task = {"ID": id, "description": args[1], "status": "Todo", "createdAt": TODAY, "updatedAt": "None"}

        #check if there are already tasks in the file and then agregate a ',' to add another object(task)
        with open(JSON_FILE, "r") as json:
            lines = json.readlines()
            if count_lines := len(lines) > 2:
                lines[count_lines-3] = '\t},\n'
                
        #remove the last line with the ']' character and then added the new task
        lines.pop()
        lines.append('\t{\n')
        for k, v in task.items():
            if k != "updatedAt":
                lines.append(f'\t\t"{k}": "{v}",\n')
        lines.append(f'\t\t"{k}": "{v}"\n')
        lines.append('\t}\n')
        lines.append(']')

        #finally rewrite the json file
        with open(JSON_FILE, "w") as json:
            json.writelines(lines)
        return f"Task added succesfully (ID: {id})"
