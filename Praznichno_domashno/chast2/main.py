import pandas as pd

#.csv файлът с покемоните го взех от github repository-то(https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv)
# на човека, чийто tutorial за pandas гледах(https://www.youtube.com/watch?v=vmEHCJofslg&ab_channel=KeithGalli)
#като цяло това, което програмата прави е, че user-a input-ва покемон елемент от изброените и след това всички покемони с този елемент биват записани в отделен .csv файл

path = input("Enter the filepath of the csv file with the pokemons: ")

data = pd.read_csv(path)
dict1 = {}

data1 = pd.DataFrame(dict1)

element = input("Enter an element(Normal, Ground, Grass, Water, Dragon, Ice,\
Fighting, Ghost, Flying, Fire, Flying, Rock, Dark, Steel, Electric, Bug, Fairy, Psychic, Rock)\
|Note: The elements must start with capital letter|: ")

data1 = pd.concat([data.loc[data['Type 1'] == element], data.loc[data['Type 2'] == element]])

data1.to_csv('Chosen_element_pokemons.csv', index = False)

print(f"\n\nYour file consists of:\n\n{data1.head(len(data1))}")
