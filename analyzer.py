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

