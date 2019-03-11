
def open_file(file_name):
    with open(file_name, "r") as file_object:
        for line in file_object:
            line = file_object.read()
    return line
