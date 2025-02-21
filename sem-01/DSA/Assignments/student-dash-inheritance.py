# Base class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def displayStudentInfo(self):
        print(f'Student name : {self.name}')
        print(f'Student age : {self.age}')


# Child class deriving/inheriting objects and properties from parent class
class Subjects(Student):
    def __init__(self,name, age, subjects,scores):
        super().__init__(name, age)
        self.subjects = subjects
        self.scores = scores
    

    def displayHighestScore(self):
        high = max(self.scores)
        ind = self.scores.index(high)

        super().displayStudentInfo()
        print(f'{self.name} has scored {high} in {self.subjects[ind]} as the highest out of all his subjects!')




students = [Subjects("Darpan Bhattacharya",21,['DSA','ML','LAMC'],[100,90,70]),Subjects("Soham Bhattacharya",21,['DSA','ML','NPTEL'],[90,90,86])]
i=1
for student in students:
    print(f'{i}th instance')
    student.displayHighestScore()
    print()
    i+=1