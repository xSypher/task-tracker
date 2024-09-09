# Task Tracker CLI in python to my backend projects
import sys
import functions as func


# Create the json file if doesn't exists
func.create_json()

# --------------- SOME CONSTANTS ---------------#
ARGV = sys.argv[1:]
COMMAND = ARGV[0]
IDV = func.get_ids()
NEXT_ID = str(len(IDV) + 1)

# ---------- MAIN LOGIC ----------#

def task_tracker():
    if COMMAND == "add":
        try:
            description = ARGV[1]
            if func.check_description() == True:
                func.add_task(description, NEXT_ID)

    elif COMMAND == "update":
        try:
            id = ARGV[1]
            if func.check_id(id, IDV) == True:
                func.update_task(ARGV[1], ARGV[2])
        
        except IndexError:
            print("ERROR: Missing ID.")

        try:
            description = ARGV[2]
            if func.check_description(description) == True:
                func.update_task(id, description)
        
        except IndexError:
            print("ERROR: Missing description.")
            
    elif COMMAND == "delete":
        try:
            id = ARGV[1]
            if func.check_id(id, IDV) == True:
                func.delete_task(id)
        
        except IndexError:
            print("ERROR: Missing ID.")
    
    elif COMMAND == "mark-in-progress":
        pass

    elif COMMAND == "mark-done":
        pass

    elif COMMAND == "list":
        pass

    else:
        print(f"Invalid command: {COMMAND}")

task_tracker()