
def load_tasks(filename: str="tasks.txt") -> list[str]:
    try:
        with open(filename,"r", encoding="utf-8") as file:
            return [line.strip()for line in file.readlines()]
    except FileNotFoundError:
        return []
def save_tasks(tasks: list[str],filename: str = "tasks.txt") -> None:
    with open(filename,"w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

tasks: list[str]=load_tasks()

def add_task(task: str):
    tasks.append(task)
    save_tasks(tasks)
    
def show_tasks() -> None:
    if not tasks:
        print("The task list is empty")
        return
    
    for i ,task in enumerate(tasks,start=1):
        print(i ,task)
def delete_task(index: int):
    if 1 <= index <= len(tasks):
        deleted=tasks.pop(index-1)
        print(f"Deleted task {deleted}")
        save_tasks(tasks)
    else:
        print("Error there is no such number")

        
while True:
    user_input=input("add/show/delete/exit:").strip()
    parts=user_input.split(maxsplit=1)
    action=parts[0].lower() if parts else ""
    
    if action== "add":
        task = parts[1] if len(parts) > 1 else input("Enter the task:")
        
        if task.strip() == "":
            print("Error the task cannot be empty") 
            continue
        add_task(task)
        print(f"Add task {task}")       
    elif action=="show":
        show_tasks()
    elif action == "delete":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input("Enter the index:"))
            delete_task(index)
        except ValueError:
            print("Error you need to enter a number after delete!")
    elif action == "exit":
        print("Exiting at program")
        break
    else:
        
        print("Unknown team")             