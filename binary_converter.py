import string

from table import *

table = Table()


def fill_table():
    with open("binary.txt") as file:
        for index, line in enumerate(file):
            line_list = line.strip().split("\t")  # strip to remove new line
            table.store(line_list[0], line_list[1], line_list[2])


def string_to_binary(string):
    result = ""
    for letter in string:
        key = table.get(letter)
        result += key.binary
        if letter == " ":
            result += " "
    return result


fill_table()

print(string_to_binary(f"Test; rand.om characters {string.punctuation}"))
