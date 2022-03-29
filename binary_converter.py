from table import *

binary = "binary.txt"

with open(binary) as file:
    lines = file.read().split("\n")

hex_, bin_, ascii_ = [], [], []

for index, line in enumerate(lines):
    temp = line.split("\t")
    hex_.append(temp[0])
    bin_.append(temp[1])
    ascii_.append(temp[2])

table = Table()

for i in range(len(bin_)):
    table.store(hex_[i], bin_[i], ascii_[i])

word = "Today's date space"
result = ""
for letter in word:
    if letter == " ":
        letter = "Space"
    key = table.get(letter)
    result += key.binary

print(result)
