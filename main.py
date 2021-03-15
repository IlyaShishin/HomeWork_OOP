class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_course(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses \
                and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def raiting(self):
        for v in self.grades.values():
            self.ave_grades = round(sum(v) / len(v), 2)
        return self.ave_grades

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.ave_grades} '
                f'\nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}')

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.ave_grades > other.ave_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def raiting(self):
        for v in self.grades.values():
            self.ave_grades = round(sum(v) / len(v), 2)
        return self.ave_grades

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.ave_grades}'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return self.ave_grades > other.ave_grades


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


grade_student_list = {
      'Леонардо ДиКаприо' : [2, 3, 5],
      'Бред Питт' : [5, 5, 5]
    }

def ave_grade_for_course_student(grade_student_list):
    """ ave_grade_for_course_student -> Считает среднюю оценку всех студентов в рамках курса. """
    grade_list_general = []
    for v in grade_student_list.values():
        ave_grade = round(sum(v) / len(v), 2)
        grade_list_general.append(ave_grade)
        ave_grade_for_course = round(sum(grade_list_general) / len(grade_list_general), 2)
    return ave_grade_for_course


grade_lecturer_list = {
      'Клинт Иствуд' : [5, 5, 5],
      'Девид Финчер' : [7, 7, 7]
    }

def ave_grade_for_course_lecturer(grade_lecturer_list):
    """ ave_grade_for_course_lecturer -> Считает среднюю оценку всех лекторов в рамках курса. """
    grade_list_general = []
    for v in grade_lecturer_list.values():
        ave_grade = round(sum(v) / len(v), 2)
        grade_list_general.append(ave_grade)
        ave_grade_for_course = round(sum(grade_list_general) / len(grade_list_general), 2)
    return ave_grade_for_course


best_student1 = Student('Леонардо', 'ДиКаприо', 'Мужчина')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['JS']

best_student2 = Student('Бред', 'Питт', 'Мужчина')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['JS']

cool_mentor1 = Reviewer('Квентин', 'Тарантино')
cool_mentor1.courses_attached += ['Python']

cool_mentor2 = Reviewer('Кристофер', 'Нолан')
cool_mentor2.courses_attached += ['Python']

cool_mentor3 = Lecturer('Гай', 'Ричи')
cool_mentor3.courses_attached += ['JS']

cool_mentor4 = Lecturer('Дэвид', 'Финчер')
cool_mentor4.courses_attached += ['JS']

cool_mentor1.rate_hw(best_student1, 'Python', 2)
cool_mentor1.rate_hw(best_student1, 'Python', 3)
cool_mentor1.rate_hw(best_student1, 'Python', 5)

cool_mentor2.rate_hw(best_student2, 'Python', 5)
cool_mentor2.rate_hw(best_student2, 'Python', 5)
cool_mentor2.rate_hw(best_student2, 'Python', 5)

print(f'Оценки Леонардо ДиКаприо: {best_student1.grades}')
print(f'Оценки Бреда Питта: {best_student2.grades}')
print(f'Средняя оценка Леонардо ДиКаприо: {best_student1.raiting()}')
print(f'Средняя оценка Бреда Питта: {best_student2.raiting()}')
print(f'Леонард успешнее Питта? {best_student1.raiting() > best_student2.raiting()}')

best_student1.rate_course(cool_mentor3, 'JS', 9)
best_student1.rate_course(cool_mentor3, 'JS', 9)
best_student1.rate_course(cool_mentor3, 'JS', 9)

best_student2.rate_course(cool_mentor4, 'JS', 7)
best_student2.rate_course(cool_mentor4, 'JS', 7)
best_student2.rate_course(cool_mentor4, 'JS', 7)

print()
print(f'Оценки лектора Гая Ричи: {cool_mentor3.grades}')
print(f'Оценки лектора Дэвида Финчера: {cool_mentor4.grades}')
print(f'Средняя оценка лектора Гая Ричи: {cool_mentor3.raiting()}')
print(f'Средняя оценка лектора Дэвида Финчера: {cool_mentor4.raiting()}')
print(f'Гай Ричи лучше Дэвида Финчера? {cool_mentor3.raiting() > cool_mentor4.raiting()}')

print()
print(best_student1)
print()
print(best_student2)
print()
print(cool_mentor1)
print()
print(cool_mentor2)
print()
print(cool_mentor3)
print()
print(cool_mentor4)

print()
print(f'Средняя оценка всех студентов по курсу Python: {ave_grade_for_course_student(grade_student_list)}')
print()
print(f'Средняя оценка всех лекторов по курсу Python: {ave_grade_for_course_lecturer(grade_lecturer_list)}')


