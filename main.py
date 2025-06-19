from task import Task

def main():
    tasks = []
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Complete Task\n4. Exit")
        option = input("Option: ")

        if option == "1":
            title = input("Task title: ")
            t = Task(title)
            t.status = "not done"  # ❌ CODE SMELL: Acceso directo a atributo
            tasks.append(t)

        elif option == "2":
            for i in range(len(tasks)):
                print(tasks[i])  # ❌ MALA PRÁCTICA: no usar enumerate

        elif option == "3":
            try:
                idx = int(input("Task number to complete: ")) - 1
                tasks[idx].complete()
            except:
                print("Something went wrong")  # ❌ CODE SMELL: captura genérica

        elif option == "4":
            break

        else:
            print("Invalid option")
main()
