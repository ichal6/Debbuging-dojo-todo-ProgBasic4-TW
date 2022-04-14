import data_access


def list_tasks(tasks):
    for index in range(len(tasks)):
        if tasks[index][0] is True:
            print(str(index + 1) + '. [X] ' + tasks[index][1])
        else:
            print(str(index + 1) + '. [ ] ' + tasks[index][1])


def add_task(tasks):
    new_task = input("Please enter new task: ")
    tasks.append(new_task)
    return tasks


def mark_task(tasks):
    task_to_mark = int(input("Which task should be marked? "))
    task_to_mark += 1
    for index in range(len(tasks)):
        if(task_to_mark == index):
            tasks[index][1] = True
    return tasks


def main():
    tasks = []
    file_name = 'tasks.txt'
    raw_data = data_access.read_file(file_name)
    tasks = data_access.split_tasks(raw_data)
    print("Tasks file has been imported.")

    is_running = True
    while is_running:
        print('    ')
        action = input("Select action [list, add, mark]: ")
        if action == "list":
            list_tasks(tasks)
        elif action == "add":
            tasks = add_task(raw_data)
        elif action == "mark":
            tasks = mark_task(tasks)
        else:
            is_running = True

    print('Goodbye!')


main()
