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


def words(open_file):
    text = open_file

    word = ""
    for line in text:
        word += " "
        for char in line:
            word += str(char)
    list_of_words = word.split()
    print(list_of_words)
    return list_of_words


def how_many_words(words):

    lenth = len(words)
    print("how many words : ",lenth)
    return lenth
