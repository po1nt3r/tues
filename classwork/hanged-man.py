from os import  system

lives = 6
string = list(input("Enter a word: "))
reveal = ["_" for i in range(len(string))]

_ = system("cls")

char = ''
while lives >= 0:
    char = input("Enter a charachter: ")
    if char in string:
        reveal[string.index(char)] = char
    else:
        lives -= 1
    print(f"lives: {lives}, string: "+''.join(reveal))

    if reveal == string:
        break

