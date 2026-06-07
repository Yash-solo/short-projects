import time
goals = []
def add_tasks():
    n = int(input("Enter how many tasks you wants to add:"))
    for i in range(n):
        goals.append(input(f"enter your  goal{i+1}:"))

#show all task/goals
def show_all():
    for i,j in enumerate(goals,start=1):
        print(i,"-goal->",j)

#tick as completed
def tick_task():
    show_all()
    n = int(input("Enter which task you wants to tick:"))
    goals[n-1] = goals[n-1]+ " done"

#task deleting
def delete_task():
    show_all()
    n = int(input("enter which task you want to delete:"))
    goals.pop(n-1)
    
#pending tasks
def pending_tasks():
    for i in goals:
        if not i.endswith("done"):
            print(i)
        else:
            None

#completed tasks
def completed_tasks():
    for i in goals:
        if i.endswith("done"):
            print(i)
        else:
            None

for i in range(1000):
    
    print("==========TO DO APP==========")
    print("       1-Add tasks")
    print("       2-Show all tasks")
    print("       3-Tick as completed")
    print("       4-Show pending tasks")
    print("       5-Show completed tasks")
    print("       6-Delete task")
    print("       7-Exit")
    try:
        choice = int(input("Enter your choice number:"))
        if choice==1:
            add_tasks()
            print("Your tasks succesfully added ")
        elif choice ==2:
            show_all()
        elif choice ==3:
            tick_task()
            print("Your task is succesfully ticked")
        elif choice==4:
            print("\n===Pending Tasks===")
            pending_tasks()

        elif choice==5:
            print("\n===Completed Tasks===")
            completed_tasks()
        elif choice==6:
            print("\nYour task is succesfully deleted\n")
            delete_task()
        elif choice==7:
            print()
            print("Loading.........")
            time.sleep(3)
            print("Done your app is now closed")
            break
        else:
            print("Plese enter a valid number")
    except ValueError:
        print("Please Enter a Valid ==> Number <==")
        
