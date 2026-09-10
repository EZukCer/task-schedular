from task_schedular.task_manager import TaskManager
from task_schedular.task import Task

class Menu:

    def __init__(self, task_manager: TaskManager): 
        self.task_manager = task_manager

    def show_main_menu(self):
        print("\nWelcome to Task Manager")
        print("1. Create Task")
        print("2. Show Tasks")
        print("3. Delete Tasks")
        print("4. Update a Task\n")

    def handle_main_menu_choice(self, choice:int):
        match choice:
            case 1:
                self.create_task_menu()
            case 2:
                self.show_tasks()
            case 3:
                self.task_manager.delete_task()
            case 4:
                self.task_manager.update_task()
            case _:
                print("Invalid Choice")

    def create_task_menu(self):
        name = input("Please enter task Name (Example: Ping Database for Uptime)\n")
        description = input("Please enter a Description (Example: Validates Database is Up)\n")

        if self.create_task_confirmation(name, description):
            self.task_created_succesfully(self.task_manager.create_task(name, description))

    def create_task_confirmation(self, name:str, description:str) -> bool:
        while True:
            confirmed = input(f"\nConfirm you want task: (Y/N) \n\nName: {name} \nDescription: {description}\nConfirmation: ").strip().lower()

            if confirmed in ("yes", "y", "true", "t"):
                return True
            elif confirmed in ("no", "n", "false", "f"):
                return False
            else:
                print("Please State Yes or No")

    def task_created_succesfully(self, task: Task):
        print(f"Succesfully created {task.name}")

    def show_tasks(self):
        tasks = self.task_manager.show_tasks()

        for task in tasks.values():
            print("|------------------------------------|")
            print("ID: ", task.id)
            print("Name: ", task.name)
            print("Description: ", task.description)
            print("|------------------------------------|")