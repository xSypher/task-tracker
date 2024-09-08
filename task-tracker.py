# Task Tracker CLI in python to my backend projects
import sys
import functions as func

# --------------- SOME CONSTANTS ---------------#
ARGV = sys.argv[1:]
COMMAND = ARGV[0]
ID = func.get_ids()


# Create the json file if doesn't exists
func.create_json()

# ---------- MAIN LOGIC ----------#

if COMMAND == "add":
    try:
        # check if a description exists and whether it's an integer.
        description = ARGV[1]
        if isinstance(description, int):
            raise ValueError(f"ERROR: Ivalid description: {description}.")

        print(func.add_task(description, str(len(ID) + 1)))

    except IndexError:
        print("ERROR: Description is missing.")

    # Value error means that the description is valid
    except ValueError as err:
        print(err)

elif COMMAND == "update":
    # checking ID
    try:
        if ARGV[1] not in func.get_ids():
            raise ValueError("ERROR: Invalid ID.")
    except ValueError as err:
        print(err)
    except IndexError:
        print("ERROR: Missing ID")

    # checking description
    try:
        description = ARGV[2]
        if isinstance(description, int):
            raise ValueError(f"ERROR: Invalid description: {description}")

        print(func.update_task(ARGV[1], ARGV[2]))

    except IndexError:
        print("ERROR: Missing description")
    except ValueError as err:
        print(err)


elif COMMAND == "delete":
    pass

elif COMMAND == "mark-in-progress":
    pass

elif COMMAND == "mark-done":
    pass

elif COMMAND == "list":
    pass

else:
    print(f"Invalid command: {COMMAND}")


# ------------------ FUNCTIONS ------------------#
