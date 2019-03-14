def list_tasks(tasks):
    for index in range(len(tasks)):
        index = index + 1
        if tasks[i][0] == 'True':
            print(index + '. [X] ' + tasks[index][1])
        else:
            print(index + '. [ ] ' + tasks[index][1])
        

def add_task(tasks):
    new_task = input("Please enter new task: ")
    tasks.append(new_task)
    return tasks


def mark_task(tasks):
    task_to_mark = input("Which task should be marked? ")
    for index in range(len(tasks)):
        if(task_to_mark == index):
            tasks[index][1] = True
    return tasks


def main():
    tasks = []
    file_name = 'tasks.txt'
    raw_data = read_file(file_name)
    split_tasks(raw_data)
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