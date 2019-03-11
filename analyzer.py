import data_manager


def line_count(list):
    for line in list:
        lenght = len(list)
    return lenght

print(line_count(data_manager.open_file("resources/input.txt")))