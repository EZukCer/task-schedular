from task_schedular.task import Task

import random
class TaskManager:


    def __init__(self):
        self.next_id = 1
        self.tasks = {}

    def create_task(self, name, description):

        task_id = self.next_id
        task = Task(task_id, name, description)
        self.tasks[task_id] = task
        self.next_id += 1

        return task

        #go back to menu to confirm success

    def show_tasks(self):
        return self.tasks

    def delete_task(self):
        print("Deleting task...")

    def update_task(self):
        print("Updating task...")


    

