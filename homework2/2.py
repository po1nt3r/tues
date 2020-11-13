vowels = ['A','a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
string = input("Enter a string: ")
vowel_count = 0

for i in range(len(string)):
    for j in range(len(vowels)):
        if string[i] == vowels[j]:
            vowel_count += 1

print(string, '->', vowel_count)

'''
за кирилица

vowels = ['А','а', 'Ъ', 'ъ', 'О', 'о', 'У', 'у', 'Е', 'е', 'И', 'и']
string = input("Enter a string: ")
vowel_count = 0

for i in range(len(string)):
    for j in range(len(vowels)):
        if string[i] == vowels[j]:
            vowel_count += 1

print(string, '->', vowel_count)
'''