from table import *

"""
CALL FILL TABLE FIRST BEFORE DOING ANYTHING
"""

table = HashTable()


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
    Splitting the binary result into different lines is almost impossible because when trying to convert the result back
    to words, a KeyError will be thrown because the hash table doesn't have "\n". Adding "\n" to the binary.txt
    file will raise some issues

    for each letter in the word:
        get the hex code
        use the hex code to get the binary equivalent from the hash table
    """
    result = ""
    for letter in word:
        hex_code = letter_to_hex(letter)
        result += table.get(hex_code).get_binary()
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


if __name__ == '__main__':
    fill_table()
    sample_sentence = "Light theme sucks, dark theme is the best."

    to_binary = word_to_binary(sample_sentence);
    to_word = binary_to_word(to_binary)

    print(f"Original sentence:\n{sample_sentence}\n")
    print(f"Converted to binary:\n{to_binary}\n")
    print(f"Converted back to words:\n{to_word}\n")
