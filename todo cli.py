
def load_tasks(filename="tasks.txt"):
    try:
        with open(filename,"r", encoding="utf-8") as file:
            return [line.strip()for line in file.readlines()]
    except FileNotFoundError:
        return []
def save_tasks():
    with open("tasks.txt","w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
tasks=load_tasks()
def add_task(task):
    tasks.append(task)
    save_tasks()
    
def show_tasks():
    if not tasks:
        print("Список задач пуст")
        return
    
    for i ,task in enumerate(tasks,start=1):
        print(i ,task)
def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted=tasks.pop(index-1)
        print(f"Удалена задача {deleted}")
        save_tasks()
    else:
        print("Ошибка такого номера нет")

        
while True:
    user_input=input("add/show/delete/exit:").strip()
    parts=user_input.split(maxsplit=1)
    action=parts[0].lower() if parts else ""
    
    if action== "add":
        task = parts[1] if len(parts) > 1 else input("Введите задачу:")
        
        if task.strip() == "":
            print("Ошибка задача не может быть пустой!") 
            continue
        add_task(task)
        print(f"Задача добавлена {task}")       
    elif action=="show":
        show_tasks()
    elif action == "delete":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input("Введите индекс:"))
            delete_task(index)
        except ValueError:
            print("Ошибка нужно ввести число после delete!")
    elif action == "exit":
        print("Выход из программы")
        break
    else:
        print("Неизвестная команда")             