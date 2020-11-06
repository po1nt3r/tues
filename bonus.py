string = input("Enter a string: ")
string = list(string)
vowels = ['A','a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
numOfVowels = 0
for i in range(len(string)):
    for j in range(len(vowels)):
        if(string[i] == vowels[j] and numOfVowels == 0):
            string[i] = '*'
            numOfVowels += 1
    if(string[i] == ' '):
        numOfVowels = 0

print(''.join(string))