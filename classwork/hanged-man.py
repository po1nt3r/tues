from os import  system

def check(string, reveal, char):
    for i in range(len(string)):
        if char == string[i]:
            reveal[i] = char

lives = 6
string = list(input("Enter a word: "))
reveal = ["_" for i in range(len(string))]

_ = system("cls")

char = ''
while lives >= 0:
    char = input("Enter a charachter: ")
    if char in string:
        check(string, reveal, char)
    else:
        lives -= 1
    print(f"lives: {lives}, string: "+''.join(reveal))

    if reveal == string:
        break

