tasks = []

def addTask():

    task = input("Enter the task: ")
    tasks.append(task)

def delTask():
    listTask()
    i = int(input("Enter the #: "))
    tasks.pop(i-1)

def listTask():
    print("Here are the tasks:")
    for i in range(len(tasks)):
        print(i+1,". ", tasks[i], "\n")


if __name__ == "__main__":

    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if (choice) == 1:
            addTask()

        elif (choice) == 2:
            delTask()

        elif (choice) == 3:
            listTask()

        elif (choice) == 4:
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

print("Goodbye!")
