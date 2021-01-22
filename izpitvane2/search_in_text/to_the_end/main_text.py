from search_text import *

text = "Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods"
search_sentence = input("Enter what you are searching for: ")
print(f"New text: {search_and_replace_text(search_sentence.split(' '), text)}")