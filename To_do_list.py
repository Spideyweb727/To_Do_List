# Create a to do list where you list down multiple task, you have the possibility
# to view the task, change the status of the task, or delete the task
'''
task_list=[
    (Task1, status)
    (Task2, status)
]
'''
print("============To-Do List Manager============"+
      "\nA simple Python based To-Do List application for managing daily tasks.\nUsers can add, view, update, and remove tasks while tracking their status.")

print("\n\n============Main Menu============")
print("\n1. View Tasks."+
       "\n2. Add Task."+
       "\n3. Mark Task as Complete."+
       "\n4. Delete Task."+
       "\n5. Exit the program.")
print("\n=================================")

task_list=[]

while True: 
    x=input("\nEnter your choice: ")
    if x =="1":
        if not task_list:
            print("\n****Your task list is currently empty.****")
        else:
            print("\n----------------*TO-DO List*----------------")
            print(f"{"Sr.No":<10}{"Task":<35}{"Status":<15}")
            for task in range(len(task_list)):
                print(f"{(task+1):<10}{task_list[task][0]:<35}{task_list[task][1]:<15}")    
    elif x =="2":
            task_name=input("\nEnter the task: ")
            if task_name:
                status="Pending"
                taskn=[task_name,status]
                task_list.append(taskn)
                print("\nTask added successfully")
            else:
                 print("\n****Task cannot be empty. Please enter a task.****")
    elif x =="3":
            print("\n----------------*TO-DO List*----------------")
            print(f"\n{"Sr.No":<10}{"Task":<35}{"Status":<15}")
            for task in range(len(task_list)):
                print(f"{(task+1):<10}"+f"{(task_list[task][0]):<35}"+f"{(task_list[task][1]):<15}")
            comp=int(input("Enter the task number to mark as complete: "))

            if comp<=(len(task_list)):
                task_list[comp-1][1]="Complete"
                print("\nTask marked as complete successfully.")
            else:
                print("\n****Invalid task number. Please enter a valid task number.****")
    elif x =="4":
            print("\n----------------*TO-DO List*----------------")
            print(f"\n{"Sr.No":<10}{"Task":<35}{"Status":<15}")
            for task in range(len(task_list)):
                print(f"{(task+1):<10}"+f"{(task_list[task][0]):<35}"+f"{(task_list[task][1]):<15}")
            del_t=int(input("\nEnter the task number to delete: "))
            if del_t<=(len(task_list)):
                task_list.pop(del_t-1)
                print("\nTask deleted successfully")
            else:
                print("\n****Please enter the correct Task number.****")
    elif x =="5":
        print("Thank you for using the TO-DO list manager")
        break
    else:
         print("****Invalid choice. Please select an option from 1 to 5.****")