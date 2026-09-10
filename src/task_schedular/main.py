from task_schedular.menu import Menu
from task_schedular.task_manager import TaskManager


def main() -> None:
    task_manager= TaskManager()
    cli_menu = Menu(task_manager)

    while True:
        cli_menu.show_main_menu()

        try:
            choice = int(input("Please enter choice (0 to exit)\n"))

            if choice == 0:
                break

            cli_menu.handle_main_menu_choice(choice)

        except ValueError:
            print("Invalid input not a Number\n")

        

        


if __name__ == "__main__":
    main()