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
                    count += 1
    return count


def count_ratio_a_to_e(list_str):
    a = 0
    e = 0
    for element in list_str:
        if "a" in element or "A" in element:
            a += 1
        if "e" in element or "E" in element:
            e += 1
    result = a / e 
    result = round(result, 3)
    return result


def consonant_to_vowel_ratio():
    consonant = ["bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"]
    vowel = ["aeiouAEIOU"]
    consonant_count = 0
    vowel_count = 0
    for character in data_manager.open_file_string("resources/input.txt"):
        for consonant_element in consonant:
            if character in consonant_element:
                consonant_count += 1
        for vowel_elements in vowel:
            if character in vowel_elements:
                vowel_count += 1
    result = consonant_count / vowel_count
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
    #print(list_of_words)
    return list_of_words


def how_many_words(words):

    lenth = len(words)
    print("how many words : ",lenth)
    return lenth


def diferent_word_count(words):
    list_words = (words)
    counter = []

    for element in list_words:
        if element not in counter:
            counter.append(element)

    diferent_words = len(counter)
    return diferent_words



def top_10_word_count(words):
    my_dict = {}
    for i in range(len(words)):
        my_dict[words[i]] = words.count(words[i])
    sorted_words = sorted(my_dict.items(), reverse=True, key=lambda x: x[1])
    topten = sorted_words[:10]
    for ele in topten:
        print(ele)
    return topten


top_10_word_count(words(data_manager.open_file("resources/input.txt")))