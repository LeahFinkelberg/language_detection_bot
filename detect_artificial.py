def prepare_message(message):
    message_word_list = message.text.split()
    return set(message_word_list)


def prepare_dict(filepath):
    file_word_list = []
    with open(filepath, "r") as input_file:
        for line in input_file:
            file_word_list.append(line)
    return set(file_word_list)


def is_artificial(reference_message_set, reference_file_set):
    intersection_quant = len(reference_message_set.intersection(reference_file_set))
    intersection_percentage = int((intersection_quant // len(reference_message_set)) * 100)
    return intersection_percentage


def facts(language_f):
    with open("facts_about_languages.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.find(language_f) != -1:
                fact = line
    return fact






