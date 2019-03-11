
def open_file(file_name):
    level_map = []
    with open(file_name, "r") as file_object:
        for line in file_object:
            line = list(line.rstrip())
            level_map.append(line)
    return level_map



def open_file_string(file_name):
    with open(file_name, "r") as file_object:
        for line in file_object:
            line = file_object.read()
    return line

