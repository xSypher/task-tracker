# Task Tracker CLI in python to my backend projects
import sys
import functions as func


# Create the json file if doesn't exists
func.create_json()

# --------------- SOME CONSTANTS ---------------#
ARGV = sys.argv[1:]
COMMAND = ARGV[0]

# ---------- MAIN LOGIC ----------#


def task_tracker():

    if COMMAND not in [
        "add",
        "update",
        "delete",
        "mark-in-progress",
        "mark-done",
        "list",
    ]:
        print(f"ERROR: Invalid command {COMMAND}")
        return

    if COMMAND == "add":

        description = func.check_args(1, ARGV, "description")
        if description and func.check_description(description):
            func.add_task(description)

    elif COMMAND == "update":

        id = func.check_args(1, ARGV, "ID")
        description = func.check_args(2, ARGV, "description")
        if (
            id
            and func.check_id(id, COMMAND)
            and description
            and func.check_description(description)
        ):
            func.update_task(id, description)

    elif COMMAND == "delete":

        id = func.check_args(1, ARGV, "ID")
        if id and func.check_id(id, COMMAND):
            func.delete_task(id)

    elif COMMAND == "mark-in-progress":
        
        id = func.check_args(1, ARGV, "ID")
        if id and func.check_id(id, COMMAND):
            func.mark_task(id, "in-progress")

    elif COMMAND == "mark-done":

        id = func.check_args(1, ARGV, "ID")
        if id and func.check_id(id, COMMAND):
            func.mark_task(id, "done")

    elif COMMAND == "list":

        try:
            status = ARGV[1]

        except IndexError:
            status = None

        func.list_task(status)


def main():
    task_tracker()


if __name__ == "__main__":
    main()
