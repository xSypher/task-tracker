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
        try:
            for task in json.load(json_file):
                ids.append(task)
        except json.decoder.JSONDecodeError:
            return("ERROR: Something is wrong with the JSON file.")
    
    return ids


def create_json() -> None:
    if not JSON_FILE.exists():
        with open(JSON_FILE, 'w') as json_file:
            json_file.write('{\n}')


def check_id(argv, ids) -> bool:
    try:
        id = argv[1]
        if id not in ids:
            raise ValueError(f"ERROR: Invalid ID: {id}")
        return True
    
    except IndexError:
        print("ERROR: Missing ID.")
        return False

    except ValueError as err:
        print(err)
        return False


def check_description(argv) -> bool:
    try:
        if (description := argv[1]).isdigit():
            raise ValueError(f"ERROR: Ivalid description: {description}.")

        return True

    except ValueError as err:
        print(err)
        return False

    

#-------------- MAIN FUNCTIONS ---------------#
def add_task(description: str, id: str) -> None:
    task = {
        "description": description,
        "status": "Todo",
        "createdAt": TODAY,
        "updatedAt": "None",
    }

    try:
        with open(JSON_FILE, 'r') as json_file:
            tasks = json.load(json_file)
    
    except json.decoder.JSONDecodeError:
        return "ERROR: Something is wrong with the json file."
    
    with open(JSON_FILE, 'w') as json_file:
        tasks[f"{id}"] = task
        json.dump(tasks, json_file, indent=4)

    print(f"Task added succesfully. (ID: {id})")


def update_task(id: str, description: str) -> None:
    try:
        with open(JSON_FILE, 'r') as json_file:
            tasks = json.load(json_file)
            for task_id, task in tasks.items():
                if task_id == id:
                    task["description"] = description
                    task["updatedAt"] = TODAY
                    break
    
    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")

    with open(JSON_FILE, 'w') as json_file:
        json.dump(tasks, json_file, indent=4)
    
    print(f"Task updated succesfully. (ID: {id})")


def delete_task(id) -> None:
    try:
        with open(JSON_FILE, 'r') as json_file:
                tasks = json.load(json_file)
                tasks.pop(id)
        
        with open(JSON_FILE, 'w') as json_file:
            json.dump(tasks, json_file, indent=4)

        print(f"Task deleted succesfully.")
    
    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")

            
                

    
