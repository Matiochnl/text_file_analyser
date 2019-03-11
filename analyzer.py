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


def alphanumeric_character_count():
    count = 0
    alphanumeric_characters = ["qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"]
    for elem in data_manager.open_file("resources/input.txt"):
        for el in elem:
            for alphanumeric_characters_element in alphanumeric_characters:
                if el in alphanumeric_characters_element:
                    print("DUPA")
                    count += 1
    return count
