import json
from datetime import date
from pathlib import Path

TODAY = date.today().__str__()
JSON_FILE = Path("tasks.json")


#---------- OTHERS FUNCTIONS----------#

# get the ids fo the existing tasks
def get_ids() -> list:
    ids = []

    with open(JSON_FILE, "r") as json_file:
        for line in json.load(json_file):
            ids.append(line["ID"])
    
    return ids


def create_json():
    if not JSON_FILE.exists():
        with open(JSON_FILE, 'w') as json_file:
            json_file.write('[\n]')

    

#-------------- MAIN FUNCTIONS ---------------#
def add(description: str) -> str:
    id = len(get_ids()) + 1
    task = {
        "ID": id,
        "description": description,
        "status": "Todo",
        "createdAt": TODAY,
        "updatedAt": "None",
    }

    with open(JSON_FILE, 'r') as json_file:
        try:
            tasks = json.load(json_file)
        except json.JSONDecodeError:
            return "ERROR: Something is wrong with the json file."
    
    with open(JSON_FILE, 'w') as json_file:
        tasks.append(task)
        json.dump(tasks, json_file, indent=4)

    return f"Task added succesfully. (ID: {id})"


def update(id: str, description: str) -> str:
    with open(JSON_FILE, 'r') as json_file:
        tasks = json.load(json_file)
        
        for task in tasks:
            if task["ID"] == id:
                task["description"] = description
                task["updatedAt"] = TODAY

    with open(JSON_FILE, 'w') as json_file:
        json.dump(tasks, json_file, indent=4)
    return f"Task updated succesfully. (ID: {id})"

    
