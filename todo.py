import os

class Todo:
    HOME_PATH = os.path.expanduser('~')
    TODO_PATH = HOME_PATH + "/.todo/"
    LIST_PATH = TODO_PATH + "list.txt"

    def __init__(self):
        pass

    def open_todo_file(self, mode):
        """Check and create/read the todo file"""
        if (os.path.exists(self.LIST_PATH) == False):
            # Create todo file if does not exist
            try:
                os.makedirs(self.TODO_PATH, exist_ok=True)
                self.todo_file = open(self.LIST_PATH, 'w+') 
            except:
                print("Error in creating todo instance ")
        else:
            # Read exist todo file
            try:
                self.todo_file = open(self.LIST_PATH, mode)
            except:
               print("Error in reading todo file")

    def list(self):
        """List out all the tasks"""
        self.open_todo_file("r")
        tasks = self.todo_file.readlines()
        if not tasks: 
            print("You have no tasks")
        else:
            for number, task in enumerate(tasks):
                task = task.replace("\n", "")
                print(f"{number+1} {task}")
            self.todo_file.close()
    
    def add(self, add_list):
        """Append new tasks to todo file"""
        self.open_todo_file("a")
        for item in add_list:
            self.todo_file.write("[ ] " + item + "\n")
        self.todo_file.close()

    def done(self, done_list):
        """Mark tasks as complete"""
        self.open_todo_file("r")
        tasks = self.todo_file.readlines()

        # Marks completed tasks with [*].
        for i in done_list:
            tasks[i-1] = tasks[i-1].replace("[ ]", "[*]")
        self.open_todo_file("w")
        self.todo_file.writelines(tasks)
        self.todo_file.close()

    def remove(self, remove_list):
        """Remove tasks in list"""
        self.open_todo_file("r")
        tasks = self.todo_file.readlines()
        if not tasks:
            print("You have no tasks")
        else:
            # Record tasks to remove into list.
            tasks_to_remove = []
            for i in remove_list:
                tasks_to_remove.append(tasks[i-1])

            # Remove tasks in tasks_to_remove list.
            for task in tasks_to_remove:
                tasks.remove(task)

            # Write new tasks list into todo file.
            self.open_todo_file("w")
            self.todo_file.writelines(tasks)
            self.todo_file.close()

    def sort(self):
        print("sorting tasks")
        self.open_todo_file("r")
        tasks= self.todo_file.readlines()
        if not tasks:
            print("You have no tasks")
        else:
            tasks.sort()
            self.open_todo_file("w")
            self.todo_file.writelines(tasks)
            self.todo_file.close()
