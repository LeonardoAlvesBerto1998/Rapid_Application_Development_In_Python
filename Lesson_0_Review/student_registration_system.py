class Student:
    def __init__(self, name:str, age:int, test1:float, test2:float, test3:float):
        self.name = name
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

    def media(self):
        studentMedia = (self.test1 + self.test2 + self.test3)/3
        return studentMedia 

    def aproved(self):
        if self.media() < 6.0:
            return 'Failed'
        else:
            return "Aproved"

        
if __name__ == "__main__":

    student1 = Student('Leonardo', 26, 8.0, 10.0, 9.5)
    student2 = Student('Raphael', 42, 10.0, 8.0, 6.0)
    student3 = Student('Maria', 18, 5.5, 4.8, 2.4)
    student4 = Student('Renata', 24, 8.5 ,2.5, 5.0)

    classroom = [student1, student2, student3, student4]

    for students in classroom:
        print('=====================================')
        print(f'Student: {students.name}\n')
        print(f'Age: {students.age}\n')
        print(f'Media: {students.media():.3f}\n')
        print(f'Student Status: {students.aproved()}\n')
        print('=====================================')
