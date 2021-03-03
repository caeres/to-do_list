#script only to do list
#current idea:
# - every task is a string, tasks can be grouped in dictionaries with due dates or something
# - all tasks saved in a dictionary
# - file in and output as txt files? maybe csv?
# - some simple commands are shown as the script is executed (print all tasks, print groups, add tasks, remove tasks, add groups, remove tasks)
# - printing task overview when script is executed?
# - due dates? how to add?
# prolly creating and writing to a csv currently seems like the right call
# for now using a txt tho, lets go

#import csv

# start off with very simple task list: no groups, no
# created a class called to do, dont remember why (now i can just fill the dictionary with {group:list with tasks,...})
import pickle
from class_todo import ToDo


with open("data/todo_list.txt", "rb") as tdl:
    all_tasks = pickle.load(tdl)


def create_task():
    task = input("Which task should be added?")
    due_date = input("When is the task due?")
    return ToDo(due_date, task)

def create_group():
    groupname = input("Which group should be added?")
    all_tasks.update({groupname:[]})

def add_task_to_group():
    groupname = input("Which group do you want to add your task to?")
    if groupname not in all_tasks.keys():
        query = input("""That group sadly doesn't exist. 
        Do you want to add your group as a new group to your to-do list?""")
        if query == "Yes":
            create_group(query)
        else:
            print("Cancelling then.")
    else: 
        all_tasks[groupname].append(create_task())
        print(f"New task was added to the group \'{groupname}\'!")

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
        print("The current functions only include creating tasks and task groups. There is no way to manage them yet.")

#helper functions
def create_group(name):
    all_tasks.update({name:[]})

all_tasks.clear()
#print list at beginnnig
print_list()

with open("data/todo_list.txt","wb") as tdl:
    pickle.dump(all_tasks, tdl)