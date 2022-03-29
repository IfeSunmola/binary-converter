from table import *

table = HashTable()

"""
CALL FILL TABLE FIRST BEFORE DOING ANYTHING
"""


def fill_table():
    """
    fill the hash table with data from the binary.txt file
    line_list contains (in order): hex, binary, ascii
    """
    with open("binary.txt") as file:
        for line in file:
            line_list = line.strip().split("\t")
            table.store(line_list[0], line_list[1], line_list[2])


def binary_to_hex(binary):
    # convert the string to int first, then get the hex,
    # remove the 0x in front of it and convert to lower
    # ToDo: do this and letter_to_hex manually
    return hex(int(binary, 2))[2:].upper()


def letter_to_hex(letter):
    return hex(ord(letter))[2:].upper()


def word_to_binary(word):
    """
    for each letter in the word:
        get the hex code
        use the hex code to get the binary equivalent from the hash table
    """
    result = ""
    for letter in word:
        hex_value = letter_to_hex(letter)
        result += table.get(hex_value).get_binary()

        # uncomment below to give spacing to words
        # if letter == " ":
        #     result += " "
    return result


def binary_to_word(binary):
    """
    for every byte (8 digits):
        find the hex code
        use the hex code to get the ascii from the hash table
    TODO: throw a custom exception if a byte can't be formed
    """
    result = ""
    prev_index = 0
    curr_index = 8  # binaries are 8
    while curr_index <= len(binary):
        curr = binary[prev_index:curr_index]
        hex_value = binary_to_hex(curr)
        temp = table.get(hex_value)
        if temp.get_hex() == "20":  # 20 is hex for space
            result += " "
        else:
            result += temp.get_ascii()
        prev_index = curr_index
        curr_index += 8
    return result
