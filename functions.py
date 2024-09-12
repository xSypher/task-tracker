import json
from datetime import date
from pathlib import Path


# -------- CONSTANTS ----------#
TODAY = date.today().__str__()
JSON_FILE = Path("tasks.json")


# ---------- OTHERS FUNCTIONS----------#


# get the ids fo the existing tasks
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


# -------------- MAIN FUNCTIONS ---------------#
def add_task(description: str) -> None:

    id = len(get_ids()) + 1
    task = {
        "description": description,
        "status": "Todo",
        "createdAt": TODAY,
        "updatedAt": "None",
    }

    try:
        with open(JSON_FILE, "r") as json_file:
            tasks = json.load(json_file)

    except json.decoder.JSONDecodeError:
        return "ERROR: Something is wrong with the json file."

    with open(JSON_FILE, "w") as json_file:
        tasks[f"{id}"] = task
        json.dump(tasks, json_file, indent=4)

    print(f"Task added succesfully. (ID: {id})")


def update_task(id: str, description: str) -> None:
    try:
        with open(JSON_FILE, "r") as json_file:
            tasks = json.load(json_file)
            tasks[id]["description"] = description
            tasks[id]["udpateAt"] = TODAY

        with open(JSON_FILE, "w") as json_file:
            json.dump(tasks, json_file, indent=4)
            print(f"Task updated succesfully. (ID: {id})")

    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")


def delete_task(id: str) -> None:
    try:
        with open(JSON_FILE, "r") as json_file:
            tasks = json.load(json_file)
            tasks.pop(id)

        with open(JSON_FILE, "w") as json_file:
            json.dump(tasks, json_file, indent=4)

        print(f"Task deleted succesfully.")

    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")


def mark_in_progress(id: str) -> None:
    try:
        with open(JSON_FILE, "r") as json_file:
            tasks = json.load(json_file)
            tasks[id]["status"] = "in-progress"
            tasks[id]["updatedAt"] = TODAY

        with open(JSON_FILE, "w") as json_file:
            json.dump(tasks, json_file, indent=4)

        print("Task marked successfully.")

    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")


def mark_done(id: str) -> None:
    try:
        with open(JSON_FILE, "r") as json_file:
            tasks = json.load(json_file)
            tasks[id]["status"] = "Done"
            tasks[id]["updatedAt"] = TODAY

        with open(JSON_FILE, "w") as json_file:
            json.dump(tasks, json_file, indent=4)

        print("Task marked successfully.")

    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")


def list_task(status: str) -> None:

    try:
        with open(JSON_FILE, "r") as json_file:
            tasks = json.load(json_file)
            if len(tasks) == 0:
                print("There's no tasks to list.")
                return

            if status == None:
                for task_id, task in tasks.items():
                    print(f"id: {task_id}")
                    for k, v in task.items():
                        print(f"{k}: {v}")
                    print("-" * 25)

            elif status == "todo" or status == "done" or status == "in-progress":
                for task_id, task in tasks.items():
                    if task["status"].lower() == status:
                        print(f"id: {task_id}")
                        for k, v in task.items():
                            print(f"{k}: {v}")
                        print("-" * 25)

            else:
                print(f"ERROR: Invalid status: <{status}>.")

    except json.decoder.JSONDecodeError:
        print("ERROR: Something is wrong with the JSON file.")
