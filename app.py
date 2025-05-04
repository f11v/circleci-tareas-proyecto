import sys
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def create_task(title):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarea creada: {task}")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"Tarea con ID {task_id} eliminada.")

def edit_task(task_id, new_title):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = new_title
            print(f"Tarea actualizada: {t}")
            break
    else:
        print(f"No se encontró tarea con ID {task_id}")
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for t in tasks:
        print(f"{t['id']}: {t['title']}")

def main():
    if len(sys.argv) < 2:
        print("Comandos: create <titulo> | delete <id> | edit <id> <nuevo titulo> | list")
        return

    command = sys.argv[1]

    if command == "create" and len(sys.argv) == 3:
        create_task(sys.argv[2])
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    elif command == "edit" and len(sys.argv) == 4:
        edit_task(int(sys.argv[2]), sys.argv[3])
    elif command == "list":
        list_tasks()
    else:
        print("Comando inválido o argumentos incorrectos.")

if __name__ == "__main__":
    main()
