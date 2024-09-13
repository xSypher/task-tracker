# task-tracker
task tracker CLI project its an app made in python which allows you to add, update, delete, mark, and list your tasks
task-cli keeps the tasks in a JSON file.

# Installation
## clone this respository
'''
git clone https://github.com/xSypher/task-tracker
'''
# How to run the program

## Make the task-cli.py executable
__put the path where you cloned the repository__
'''
chmod +x path/to/task-tracker/task-cli.py
'''
# Ways to run the program

## 1. Make an alias for the app "Unix-like systems"
__put the path where you cloned the repository__
'''
echo 'alias task-cli="~/path/to/task-tracker/task-cli.py"' >> .bashrc
'''

## 2. Go to the directory where you cloned the repository.
'''
cd Path/to/the/repository/directory/
'''
'''
./task-cli.py add "my first task"

# Usage:
__task-cli <command> <parameters>__

## __Commands__:

### add command:
this task will add a task, it only receives non integers descriptions
__usage__: __"add description"__
'''
./task-cli.py add "buy something"
'''
__good description: "cook"__
__bad description: 1__








project URL: [https://roadmap.sh/projects/task-tracker]