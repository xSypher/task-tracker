import os
import json
from datetime import date
from pathlib import Path


# -------- CONSTANTS ----------#
TODAY = date.today().strftime("%m/%d/%y")
dir_path = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = Path(str(dir_path) + "/tasks.json")

# -------------- MAIN FUNCTIONS ---------------#
def add_task(description: str) -> None:

    id = len(get_ids()) + 1
    task = {
        "description": description,
        "status": "Todo",
        "createdAt": TODAY,
        "updatedAt": "None",
    }

    tasks = load_tasks()
    tasks[f"{id}"] = task
    save_tasks(tasks)
    print(f"Task added succesfully. (ID: {id})")


def update_task(id: str, description: str) -> None:
    
    tasks = load_tasks()
    tasks[id]["description"] = description
    tasks[id]["updatedAt"] = TODAY
    save_tasks(tasks)
    print(f"Task updated succesfully. (ID: {id})")


def delete_task(id: str) -> None:
   
    tasks = load_tasks()
    tasks.pop(id)
    save_tasks(tasks)
    print(f"Task deleted succesfully.")


def mark_task(id: str, status: str) -> None:
    
    tasks = load_tasks()
    tasks[id]["status"] = status
    tasks[id]["updatedAt"] = TODAY
    save_tasks(tasks)
    print("Task marked succesfully.")
        

def list_task(status: str | None) -> None:
    
    tasks = load_tasks(status)
    try:
        if len(tasks) == 0:
            print("There's no tasks to list.")
            return
    
        elif len(tasks) > 0:
            print("-"*40)
            for id, task in tasks.items():
                print(f'ID: {id}')
                for k, v in task.items():
                    print(f"{k}: {v}")
                print("-"*40)
    
    except TypeError:
        pass
    
# ---------- OTHERS FUNCTIONS----------#

def get_ids() -> list:
    ids = []

    with open(JSON_FILE, "r") as json_file:
        try:
            for task in json.load(json_file):
                ids.append(task)
        except json.decoder.JSONDecodeError:
            return "ERROR: Something is wrong with the JSON file."

    return ids


def create_json() -> None:
    if not JSON_FILE.exists():
        with open(JSON_FILE, "w") as json_file:
            json_file.write("{\n}")


def check_args(
    index: int,
    args: list,
    arg="argument",
):
    try:
        return args[index]

    except IndexError:
        print(f"ERROR: Missing {arg}.")
        return None


def check_id(id, command) -> bool:
    ids = get_ids()
    try:
        if len(ids) == 0:
            print(f"There's no tasks to {command}.")
            return False

        elif id not in ids:
            raise ValueError(f"ERROR: Invalid ID: {id}")

        return True

    except ValueError as err:
        print(err)
        return False


def check_description(description: str) -> bool:
    try:
        if description.isdigit():
            raise ValueError(f"ERROR: Invalid description: {description}.")

        return True

    except ValueError as err:
        print(err)
        return False
    

def load_tasks(status=None) -> dict:
    
    tasks = {}
    
    if status not in ["in-progress", "done", "todo"] and status != None:
        print(f"ERROR: Invalid status <{status}>")
        return None
    
    try:
        with open(JSON_FILE, 'r') as json_file:
            
            tasks = json.load(json_file)
            
            if status == None:
                return tasks
            
            if len(tasks) > 0:
                tasks = {id: task for id, task in tasks.items() if task["status"] == status}
            
            return tasks
            
    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")


def save_tasks(tasks) -> None:
    
    try:
        with open(JSON_FILE, 'w') as json_file:
            json.dump(tasks, json_file, indent=4)
            
    except TypeError:
        print("ERROR: Can't save the tasks, try again.")