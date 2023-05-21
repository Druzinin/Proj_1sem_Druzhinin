# Вариант 27

class Student:
    def __init__(self, name: str, surname: str, grades: list):
        self.name = name
        self.surname = surname
        self.grades = grades

    def gpa(self):
        return sum(lst) / len(lst) if (lst := self.grades) else 0.0

    def is_excellent(self):
        return 'Отличник' if set(self.grades) == {5} else 'Не отличник'


excellent = Student('Иван', 'Иванов', [5, 5, 5, 5, 5])
poor = Student('Петр', 'Петров', [2, 3, 2, 3, 2])
no_grades = Student('Анна', 'Сидорова', [])

print('Студент с отличными оценками:')
print(f'Средний балл - {excellent.gpa()} -> {excellent.is_excellent()}\n')

print('Студент с плохими оценками:')
print(f'Средний балл - {poor.gpa()} -> {poor.is_excellent()}\n')

print('Студент без оценок:')
print(f'Средний балл - {no_grades.gpa()} -> {no_grades.is_excellent()}\n')
