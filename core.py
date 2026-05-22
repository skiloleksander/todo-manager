from datetime import datetime
import json
import os

todo: list[dict] = list()
filename = "todo.json"
add_counter = 0
complete_counter = 0

TASK_TYPES: dict[str, dict] = {
    "1": {
        "value": "default",
        "label": "Звичайний",
        "completable": True,
        "extra_fields": {}
    },
    "2": {
        "value": "deadline",
        "label": "З дедлайном",
        "completable": True,
        "extra_fields": {"deadline": None}
    },
    "3": {
        "value": "schedule",
        "label": "Розклад",
        "completable": False,
        "extra_fields": {"time_start": None, "time_end": None}
    },
    "4": {
        "value": "recurring",
        "label": "Зробити декілька разів",
        "completable": True,
        "extra_fields": {"times_total": None, "times_done": 0}
    },
}

def validate(index: int):
    if index < 1 or index > len(todo):
        raise IndexError("Невірний індекс.")

def write_in_file():
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(todo, file, ensure_ascii=False, indent=2)

def history_log():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("todo_history.txt", 'a', encoding='utf-8') as file:
        file.write(
            f"Всього доданих завдань: {add_counter}\n"
            f"Всього виконаних завдань: {complete_counter}\n"
            f"Дата логу: {date}\n"
            "---\n"
        )

def create_task(text: str, type_key: str, **extra):
    task_type = TASK_TYPES.get(type_key)
    if task_type is None:
        raise ValueError(f"Невідомий тип завдання: {type_key}")
    task = {
        "id": todo[-1]["id"] + 1 if todo else 1,
        "task": text,
        "type": task_type['value'],
        **task_type["extra_fields"],
        **extra
    }
    if task_type["completable"]:
        task["is_completed"] = False
    return task

def add_todo(task: dict):
    global add_counter
    todo.append(task)
    add_counter += 1
    write_in_file()

def get_todo(index: int):
    validate(index)
    return todo[index - 1]

def get_all_todo():
    return todo

def edit_todo(index: int, new_text: str):
    validate(index)
    todo[index - 1]["task"] = new_text
    write_in_file()

def complete_todo(index: int):
    global complete_counter
    validate(index)
    task = todo[index - 1]
    if task["type"] == "schedule":
        raise ValueError("Ця тудушка є розкладом, його не можна виконати.")
    if task["type"] == "recurring":
        if task["is_completed"] == False:
            task["times_done"] += 1
            if task["times_done"] >= task["times_total"]:
                task["is_completed"] = True
                complete_counter += 1
        else:
            task["times_done"] = 0
            task["is_completed"] = False
            complete_counter -= 1
    elif task["is_completed"] == False:
        task["is_completed"] = True
        complete_counter += 1
    else:
        task["is_completed"] = False
        complete_counter -= 1
    write_in_file()
    
def delete_todo(index: int):
    validate(index)
    todo.pop(index - 1)
    write_in_file()

def count_todos():
    return len(todo)

def clear_todos():
    todo.clear()
    write_in_file()

def backup():
    os.makedirs("data", exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backupfilename = f"data/todo_backup_{now}.json"
    with open(backupfilename, 'w', encoding='utf-8') as file:
        json.dump(todo, file, ensure_ascii=False, indent=2)

def load_todo():
    todo.clear()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                return
            data = json.loads(content)
            todo.extend(data)
    except FileNotFoundError:
        open(filename, 'w', encoding='utf-8').close()

def load_from_backup(backupfilename: str):
    print("=========================",backupfilename)
    with open(backupfilename, 'r', encoding='utf-8') as file:
        try:
            content = file.read().strip()
            if not content:
                return
            data = json.loads(content)
            todo.clear()
            todo.extend(data)
        except:
            raise FileNotFoundError
    write_in_file()