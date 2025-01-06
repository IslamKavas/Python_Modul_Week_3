
#To begin creating an empty list and a counter 
task_list = {}
task_squence = 100

#Loop for start menu
while True:

    print("Task Manager System\n")

    print("Please choose one of the actions below.\n")

    print("1. Add a new task")
    print("2. Complete a task")
    print("3. Delete a task")
    print("4. List completed tasks")
    print("5. List all tasks with their status")
    print("6. Exit\n")

    choice = input("Please enter the action number you would like to take: ")
    
    
    if choice == '1':
        #Add a new task
        task_squence += 1
        task_name = input("Please enter a name for the task: ")
        task_list[task_squence] = {'name' : task_name, 'status' : 'Incomplete'} 
        print(f"\nThe new task named {task_name} is listed with {task_squence} task ID.\n")


    elif choice == '2':
        #Complete a task
        task_id = int(input("Please enter the task ID: "))

        if task_id in task_list:
            task_list[task_id]['status'] = 'Completed'

            print(f"\nThe task {task_id} is completed.\n")
        else:
            print("\nTask ID not found.\n")
        


    elif choice == '3':
        #Delete a task

        task_id = int(input("Please enter a task ID to be deleted: "))
        if task_id in task_list:
            del task_list[task_squence]

        print(f"The task {task_id} is deleted.\n")

    elif choice == '4':
        # List completed tasks
        print("Completed Tasks:")
        for task_id, task in task_list.items():
            if task['status'] == 'Completed':
                print(f"ID: {task_id}, Name: {task['name']}")
        if not any(task['status'] == 'Completed' for task in task_list.values()):
            print("No completed tasks found.\n")
           
           

        

    elif choice == '5':
        #List all tasks with their status
        for task_id, task in task_list.items():
           
            print(f"ID: {task_id}, Name: {task['name']}, Status: {task['status']}\n")


        print("The tasks and their status are listed.\n")

    elif choice == '6':
        print("Exiting the task manager system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again!")
