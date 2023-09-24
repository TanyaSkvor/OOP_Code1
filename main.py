class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecture_grades = {}

    def _average_grade(self):
        grades_lec = 0
        count = 0
        for course in list(self.courses_attached):
            for i in self.lecture_grades[course]:
                grades_lec += int(i)
                count += 1
        return grades_lec / count

    def __str__(self):
        lect = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return lect
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rev = f'Имя: {self.name}\nФамилия: {self.surname}'
        return rev

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lect_grd(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'
    def _average_homework_grade(self):
        grades_hw = 0
        count = 0
        for course in self.courses_in_progress:
            for i in self.grades[course]:
                grades_hw += int(i)
                count += 1
        return grades_hw / count
    def __str__(self):
        std = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_homework_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return std

# Создаем экземпляры класса экспертов
ivan_abramov = Reviewer('Иван', 'Абрамов')
egor_ivanov = Reviewer('Егор', 'Иванов')

# Создаем экземпляры класса лекторов
george_krivin = Lecturer('Георгий', 'Кривин')
ivan_petrov = Lecturer('Иван', 'Петров')

# Создаем экземпляры класса студентов
tanya_selezneva = Student('Таня', 'Селезнева', 'woman')
pavel_mamaev = Student('Павел', 'Мамаев', 'man')

# Добавление информации к экземплярам
george_krivin.courses_attached += ['Git','Python']
ivan_abramov.courses_attached += ['Git']
egor_ivanov.courses_attached += ['Python']
tanya_selezneva.courses_in_progress += ['Git', 'Python']
tanya_selezneva.finished_courses += ['Введение в программирование']
pavel_mamaev.courses_in_progress += ['Git', 'Python']
tanya_selezneva.lect_grd(george_krivin, 'Git', 8)
tanya_selezneva.lect_grd(george_krivin, 'Python', 7)
pavel_mamaev.lect_grd(george_krivin, 'Git', 9)
ivan_abramov.rate_hw(tanya_selezneva, 'Git', 10)
egor_ivanov.rate_hw(tanya_selezneva, 'Python', 9)

# Вывод данных
print(ivan_abramov)
print(george_krivin)
print(tanya_selezneva)
