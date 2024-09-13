# task-tracker
task tracker CLI project.

its an app made in python which allows you to add, update, delete, mark, and list your tasks. 
task-cli keeps the tasks in a JSON file.

# Installation
__clone this respository__

```
git clone https://github.com/xSypher/task-tracker`
```

# How to run the program

## Make the task-cli.py file executable

put the path where you cloned the repository
```
chmod +x path/to/task-tracker/task-cli.py
```
## Ways to run the program
### 1. Make an alias for the app. Only Unix-like systems.
put the path where you cloned the repository
```
echo 'alias task-cli="~/path/to/task-tracker/task-cli.py"' >> .bashrc
```

### 2. Go to the directory where you cloned the repository.
```
-cd Path/to/the/repository/directory/

-./task-cli.py add "my first task"
```
-----------------------------------------------------------
# Usage:
`task-cli <command> <parameters>`
`./task-cli.py <command> <parameters> `


## Commands:
### add:
this command adds a task, it only receives non integers descriptions.
### usage:
`task-cli add <description>`
### example:
```
task-cli add "buy something"
```
__good description: "cook"__

__bad description: 1__

---------------------------------------------------------

### update:
this command updates the description of a task.
### usage:
`task-cli update <id> <description>`
### example:
```
task-cli update 1 "buy somthing and cook"
```
---------------------------------------------------------

### delete command
this command deletes a task.
### usage:
`task-cli delete <id>`
### example:
```
task-cli delete 1
```

---------------------------------------------------------

### mark-in-progress command
this command marks as "in-progress" the status of a task.
### usage:
`task-cli mark-in-progress <id>`
### example:
```
task-cli mark-in-progress 1
```

---------------------------------------------------------

### mark-done command
this command marks as "done" the status of a task.
### usage:
`task-cli mark-done <id>`
### example:
```
task-cli mark-done 1
```

---------------------------------------------------------

### list command
this command lists all tasks.
### usage:
`task-cli list`

### list by status
list command receive a parameter wich must be the status of the tasks that we want to list

__status:__
`todo`
`in-progress`
`done`

### example:
``` 
task-cli list


task-cli list todo

task-cli list in-progress

task-cli list done
```
-----------------------------------------------------------------------
## That's all you need to know to use this CLI app. Thanks and enjoy it.
### This project idea is from: https://roadmap.sh/projects/task-tracker