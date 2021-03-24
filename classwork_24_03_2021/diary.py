import json
import os

class Uchenik:
    def __init__(self, number_in_class, name, grades = None):
        self.number_in_class = number_in_class
        self.name = name
        if not grades:
            self.grades = self.enter_grades()
        else:
            self.grades = grades

    def enter_grades(self):
        num_grades = int(input("Enter number of grades: "))
        grades = []
        for _ in range(num_grades):
            grades.append(int(input("Enter grade: ")))

        return grades

class Dnevnik:
    def __init__(self, num_of_students):
        self.diary_dict = {}
        if os.path.exists("diary.json"):
            self.students = self.read_diary()
            self.num_of_students = len(self.students)
        else:
            self.students = self.enter_students(num_of_students)
            self.num_of_students = num_of_students
            
    
    def enter_students(self, num_of_students):
        students = []
        for _ in range(num_of_students):
            a = Uchenik(int(input("Enter number in class: ")), input("Enter name: "))
            students.append(a)
        
        return students

    def write_diary(self):
        self.diary_dict = {}
        for i in range(self.num_of_students):
            self.diary_dict[self.students[i].number_in_class] = dict({"name": self.students[i].name, 
            "grades": self.students[i].grades})
        
        with open("diary.json", "w") as fw:
            json.dump(self.diary_dict, fw, indent = 4)
    
    def read_diary(self):
        with open("diary.json", "r") as fr:
            self.diary_dict = json.load(fr)
        num_of_students = len(self.diary_dict)
        numbers = list(self.diary_dict.keys())
        values = list(self.diary_dict.values())
        students = []
        for i in range(num_of_students):
            a = Uchenik(numbers[i], values[i]["name"], values[i]["grades"])
            students.append(a)
        
        return students

diary = Dnevnik(1)
diary.write_diary()
