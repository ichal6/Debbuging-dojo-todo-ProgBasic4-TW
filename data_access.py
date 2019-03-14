def read_file(file_name):
    raw_data = []
    with open('file_name', 'r') as file:
        for line in file:
            raw_data.append(line)
            return raw_data
        


def split_tasks(raw_data):
    tasks = []
    for line in raw_data:
        splitted = line.split('|')
        
        task = []
        task.append(bool(splitted[0]))
        task.append(splitted[1])

        tasks.append(task)

    return tasks