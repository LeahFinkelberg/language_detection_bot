import re

henllinge_word_list = []

with open("Hen_llinge.txt", "r+") as input_file:
    for line in input_file:
        line = re.sub(r"\[\d\]", r"", line, count=0)
        line = re.sub(r"[a-z]+,", r"", line, count=0)
        line_list = line.split(" ")
        henllinge_word_list.append(line_list[0])

with open("Hen_llinge_words.txt", "w") as output_file:
    output_file.write("\n".join(henllinge_word_list))
