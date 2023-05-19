sindarin_word_list = []

with open("Sindarin.txt", "r+") as input_file:
    for line in input_file:
        line_list = line.split(" ")
        sindarin_word_list.append(line_list[0])

with open("Sindarin_words.txt", "w") as output_file:
    output_file.write("\n".join(sindarin_word_list))
