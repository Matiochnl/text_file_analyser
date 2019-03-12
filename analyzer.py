import data_manager
import datetime


def read_from_file():
    result = data_manager.open_file("resources/input.txt")
    return result


def character_count():
    count = 0
    for file_element in data_manager.open_file("resources/input.txt"):
        for element in file_element:
            if element == " ":
                count = count
            else:
                count += 1
    return count


def line_count(file_object):
    file_object = read_from_file()
    return len(file_object)


def alphanumeric_character_count():
    count = 0
    alphanumeric_characters = [
        "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"]
    for file_element in data_manager.open_file("resources/input.txt"):
        for element in file_element:
            for alphanumeric_characters_element in alphanumeric_characters:
                if element in alphanumeric_characters_element:
                    count += 1
    return count


def count_ratio_a_to_e():
    a = 0
    e = 0
    for element in data_manager.open_file_string("resources/input.txt"):
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


def change_letters_into_words(open_file):
    text = open_file

    word = ""
    for line in text:
        word += " "
        for char in line:
            word += str(char)
    list_of_words = word.split()
    # print(list_of_words)
    return list_of_words


def how_many_words(words):

    lenght = len(words(read_from_file()))
    return lenght


def diferent_word_count(change_letters_into_words):
    list_of_words = (change_letters_into_words(open_file=read_from_file()))
    counter = []

    for element in list_of_words:
        if element not in counter:
            counter.append(element)

    diferent_words = len(counter)
    return diferent_words


def top_10_word_count(change_letters_into_words):
    results = {}
    change_letters_into_words = change_letters_into_words(open_file=read_from_file())
    for i in range(len(change_letters_into_words)):
        results[change_letters_into_words[i]] = change_letters_into_words.count(change_letters_into_words[i])
    sorted_words = sorted(results.items(), reverse=True, key=lambda x: x[1])
    topten = sorted_words[:10]
    return topten


def save_to_file():
    results = [str(character_count()) + ": Character amount",
               str(line_count(file_object=read_from_file())) + ": Line amount",
               str(alphanumeric_character_count()) +
               ": Alphanumeric character amount", change_letters_into_words(
               open_file=read_from_file()),
               str(how_many_words(change_letters_into_words)) + ": How many words in file", str(
                   diferent_word_count(change_letters_into_words)) + ": Words not repeated",
               str(top_10_word_count(change_letters_into_words)) + ": How many times words are used"]
    actual_time = datetime.datetime.now()
    filename = "{year}_{month}_{day}__{hour}_{minutes}_{seconds}.txt".format(
        year=actual_time.year,
        month=actual_time.month,
        day=actual_time.day,
        hour=actual_time.hour,
        minutes=actual_time.minute,
        seconds=actual_time.second)

    data_manager.write_data_to_file(results, filename)


def sort_by_appearance_count(change_letters_into_words):
    my_dict = {}
    for i in range(len(change_letters_into_words)):
        my_dict[change_letters_into_words[i]] = change_letters_into_words.count(change_letters_into_words[i])
    sorted_words = sorted(my_dict.items(), reverse=True, key=lambda x: x[1])
    return sorted_words


save_to_file()