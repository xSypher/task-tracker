#Task Tracker CLI in python to my backend projects
import sys 
import functions as func

#--------------- SOME CONSTANTS ---------------#
ARGV = sys.argv[1:]
COMMAND = ARGV[0]
JSON_FILE = "tasks.json"

#Create the json file if doesn't exists
try:
    open(JSON_FILE, "x")
    with open(JSON_FILE, "w") as json:
        json.write('[\n]')
except FileExistsError:
    pass

ID = func.get_ids() # List for the tasks' IDs
#---------- MAIN LOGIC ----------#

if COMMAND == "add":
    try:
        print(func.add(ARGV, len(ID)+1))
    except IndexError as err:
        print(err)
    except ValueError as err:
        print(err)

elif COMMAND == "update":
    try:
        int(ARGV[1]) #check if ARGV[1] is a valid ID(integer).
        ARGV[2] #check if there's a description.
        if len(ARGV) == 3 and ARGV[2] == str:
            update(ARGV[1], ARGV[2])
    except ValueError:
        print(f"ERROR: Invalid ID argument: {ARGV[1]}")
    except IndexError:
        print("ERROR: description is missing.") 
    else:
        print(f"ERROR: Invalid argument: {ARGV.pop()}")

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





#------------------ FUNCTIONS ------------------#








    
