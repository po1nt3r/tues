import os
import requests

#част от файловете в github. Иначе са твърде много
folders = ["04.12.2020/izpitvane.py", "24_02_2021/test.py", "Homework_24_02_2021/bank_account_json.py", "Homework_24_02_2021/bank_account_yaml.py",
           "bank/bank.py", "classwork/hanged-man.py", "classwork3/classwork_13.11.py", "classwork3/exercise1_13.11.py", "classwork3/exercise2_13.11.py",
           "classwork3/exercise3_13.11.py", "classwork3/exercise4_13.11.py"]
try:
    os.mkdir("git_files")
except FileExistsError:
    pass

file_path = "https://raw.githubusercontent.com/AlekoGeorgiev/tues/main/"
os.chdir("git_files")

for i in folders:
    j = i.split("/")[0]
    try:
        os.mkdir(j)
    except FileExistsError:
        pass
    r = requests.get(file_path + i)
    with open(f"../git_files/{i}", "wb") as f:
        for i in r.iter_content(chunk_size=8192):
            f.write(i)