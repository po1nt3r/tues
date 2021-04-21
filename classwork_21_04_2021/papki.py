import os
import random


num_of_files = int(input("Enter number of files: "))

os.mkdir("folders")

    
for i in range(num_of_files):
    os.mkdir(f"folders/folder{i}")
    random_int = random.randint(0, 10)
    
    for j in range(random_int):
        with open(f"folders/folder{i}/file{j}.txt", "w") as fw:
            fw.write(str(j))
