import pickle
from class_todo import ToDo
import os


if "todo_list.txt" not in os.listdir("data"):
    with open("data/todo_list.txt", "x") as tdl:
        all_tasks = {}
else:
    with open("data/todo_list.txt", "r+") as tdl:
        all_tasks = pickle.load(tdl)


      
def create_todo():
    task = input("What task should be added?")
    due_date = input("When is the task due?")
    return ToDo(due_date, task)

#creating tasks and groups
def create_group_in():
    groupname = input("Which group should be added?")
    all_tasks.update({groupname:[]})
    print_list()

def create_group(name):
    all_tasks.update({name:[]})
    print_list()

def add_task_to_group():
    groupname = input("Which group do you want to add your task to?")
    if groupname not in all_tasks.keys():
        query_nogroup = groupname
        query = input("""That group sadly doesn't exist. 
        Do you want to add your group as a new group to your to-do list?""")
        if query == "Yes":
            create_group(query_nogroup)
        else:
            print("Cancelling then.")
    else: 
        all_tasks[groupname].append(create_todo())
        print(f"New task was added to the group \'{groupname}\'!")
    print_list()    
#deleting tasks and groups
def delete_group():
    groupname = input("Which group should be deleted?")
    if groupname in all_tasks:
        del all_tasks[groupname]
    else: 
        print("This group is not included in your to-do list so far. Please try again!")
    print_list()
def delete_task():
    task = input("Which task should be deleted?")
    due = input("When is the task due?")
    to_delete = ToDo(due, task)
    for key in all_tasks.keys():
        for item in all_tasks[key]:
            if item.check_equal(to_delete):
                all_tasks[key].remove(item)
    print_list()

#printing the list to console
def print_list():
    print("YOUR TO-DO LIST:\n")
    if all_tasks != {}:
        for key in all_tasks:
            print(key.upper())
            group_list = all_tasks[key]
            if group_list != []:
                i = 1
                for item in group_list:
                    print(f"({i}) {item}")
                    i += 1
            else: 
                print("-empty group-")
            print("\n")
    else:
        print("""Seems like this is your first time using this script! Getting started is no problem,
        you can kick off your personal to-do list using the commands below. Just create a group, add some
        tasks to it and play around with the script!""")
    print("""You can currently use the commands: \"Print List\", \"Create Task\", \"Create Group\", \"Delete Task\"
    and \"Delete Group\". To close this program, enter \"Exit\".""")

#print list at beginnnig
print_list()
#while loop to keep the programm running
command = input("What do you want to do?")
while command != 'Exit':
    if command == "Create Task":
        add_task_to_group()
        command = input("What do you want to do?")
    elif command == "Create Group":
        create_group_in()
        command = input("What do you want to do?")
    elif command == "Print List":
        print_list()
        command = input("What do you want to do?")
    elif command == "Delete Task":
        delete_task()
        command = input("What do you want to do?")
    elif command == "Delete Group":
        delete_group()
        command = input("What do you want to do?")
    else:
        print("That command sadly doesn't exist.")
        command = input("What do you want to do?")
    if command=="Exit":
        print("Goodbye!")
    

with open("data/todo_list.txt","wb") as tdl:
    pickle.dump(all_tasks, tdl)