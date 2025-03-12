class Student:
    def __init__(self, name, surname, year_of_study, field_of_study, grade):
        self.name = name
        self.surname = surname
        self.year_of_study = year_of_study
        self.field_of_study = field_of_study
        self.grade = grade

    def graduation(self, grade, year_of_study):
        if grade == 'lic':
            years = 3
            years -= year_of_study
            return print(years)
        elif grade == 'mgr':
            years = 5
            years -= year_of_study
            return print(years)
    
    def show_student_info(self):
        return print(f'{self.name} {self.surname} {self.year_of_study} {self.field_of_study} {self.grade}')
        
student1 = Student('Kacper', 'Wrona', 1, 'Big Data', 'lic')
student1.graduation('lic', 1)
student1.show_student_info()


