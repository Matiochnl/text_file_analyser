import data_manager


def character_count():
    count = 0
    for elem in data_manager.open_file("resources/input.txt"):
        for el in elem:
            if el == " ":
                count = count
            else:
                count += 1
        return count


def line_count(list):
    for line in list:
        lenght = len(list)
    return lenght


def count_ratio_a_to_e(list_str):
    a = 0
    e = 0
    for element in list_str:
        if "a" in element:
            a += 1
        if "e" in element:
            e += 1
    result = a / e 
    result = round(result, 3)
    return result

