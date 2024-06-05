string = input("Enter a string: ")
string = string.lower()

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_frequent = None
highest_count = 0

for char, count in char_count.items():
    if count > highest_count:
        most_frequent = char
        highest_count = count

print(f"The character that appears most frequently in the string is {most_frequent}.")