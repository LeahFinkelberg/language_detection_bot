qwenya_word_list = []

with open("Qwenya.txt", "r+") as input_file:
    for line in input_file:
        line_list = line.split(" ")
        qwenya_word_list.append(line_list[0])

with open("Qwenya_words.txt", "w") as output_file:
    output_file.write("\n".join(qwenya_word_list))
