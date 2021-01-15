word = input("Enter a word: ")
hidden = ['_' for i in range(len(word))]

class Hanged_man:
    def __init__(self, word, hidden, lives):
        self.word = list(word)
        self.hidden = list(hidden)
        self.lives = lives
    
    in_the_string = False
    def in_string(self, letter):
        for i in range(len(self.word)):
            if letter == self.word[i]:
                self.hidden[i] = letter
                self.in_the_string = True
        
        if self.in_the_string == False:
            self.lives -= 1
        
        self.in_the_string = False
    
    def win(self):
        if self.hidden == self.word:
            return True
        else:
            return False
    
    def print_hidden_lives(self):
        print(self.hidden)
        print(f"Remaining lives: {self.lives}")
    
hanged = Hanged_man(word, hidden, 8)

while hanged.lives > 0:
    letter = input("Enter a letter: ")
    hanged.in_string(letter)
    hanged.print_hidden_lives()
    if hanged.win():
        print('You won')
        break
    
if hanged.lives == 0:
    print("You lost")

