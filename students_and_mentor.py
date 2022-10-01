class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Не лектор'

    def average_grades_hmwork(self):
        midle_python_stu = sum(self.grades['Python']) / len(self.grades['Python'])
        midle_git_stu = sum(self.grades['Git']) / len(self.grades['Git'])
        midle_grades_stu = (midle_python_stu + midle_git_stu) / len(self.grades)
        return round(midle_grades_stu, 1)

    def __str__(self):
        student_line = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за ДЗ: ' \
                       f'{self.average_grades_hmwork()}\n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n Завершенные курсы: ' \
                       f'{" ".join(self.finished_courses)}'
        return student_line

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Не студент'
        bool_var = self.average_grades_hmwork() > other.average_grades_hmwork()
        if bool_var == True:
            return f'Средняя оценка у студента {self.name} больше {other.name}'
        if bool_var == False:
            return f'Средняя оценка у студента {self.name} меньше {other.name}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def average_grades_courses(self):
        midle_python_lec = sum(self.course_grades['Python']) / len(self.course_grades['Python'])
        midle_git_lec = sum(self.course_grades['Git']) / len(self.course_grades['Git'])
        midle_grades_Lec = (midle_python_lec + midle_git_lec) / len(self.course_grades)
        return round(midle_grades_Lec, 1)

    def __str__(self):
        lecturer_line = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: ' \
                        f'{self.average_grades_courses()}'
        return lecturer_line

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не преподаватель'
        bool_var = self.average_grades_courses() > other.average_grades_courses()
        if bool_var == True:
            return f'Средняя оценка у лектора {self.name} больше {other.name}'
        if bool_var == False:
            return f'Средняя оценка у лектора {self.name} меньше {other.name}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Не студент'

    def __str__(self):
        reviewer_line = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return reviewer_line

################### student1 ##############################
student1 = Student('Том', 'Том1', 'он')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Git']

#################### student2 #############################
student2 = Student('Тим', 'Тим1', 'оно')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Python']

################### lecturer1 ##############################
lecturer1 = Lecturer('Кук', 'Кук1')
lecturer1.courses_attached += ['Python', 'Git']

#################### lecturer2 #############################
lecturer2 = Lecturer('Кик', 'Кик2')
lecturer2.courses_attached += ['Python', 'Git']

################ reviewer1 #################################
reviewer1 = Reviewer('Пук', 'Пук1')
reviewer1.courses_attached += ['Python', 'Git']

################# reviewer2 ###############################
reviewer2 = Reviewer('Пик', 'Пик1')
reviewer2.courses_attached += ['Python', 'Git']

################### student1 ###########################
student1.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 3)
student1.rate_lecturer(lecturer1, 'Git', 6)
student1.rate_lecturer(lecturer1, 'Git', 4)
student1.rate_lecturer(lecturer1, 'Git', 8)

#################### student2 #########################
student2.rate_lecturer(lecturer2, 'Python', 4)
student2.rate_lecturer(lecturer2, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 8)
student2.rate_lecturer(lecturer2, 'Git', 9)
student2.rate_lecturer(lecturer2, 'Git', 8)

#################### reviewer1 #######################
reviewer1.rate_student(student1, 'Python', 8)
reviewer1.rate_student(student1, 'Python', 5)
reviewer1.rate_student(student1, 'Python', 2)
reviewer1.rate_student(student1, 'Git', 9)
reviewer1.rate_student(student1, 'Git', 10)
reviewer1.rate_student(student1, 'Git', 3)

################### reviewer2 #########################
reviewer2.rate_student(student2, 'Python', 9)
reviewer2.rate_student(student2, 'Python', 6)
reviewer2.rate_student(student2, 'Python', 10)
reviewer2.rate_student(student2, 'Git', 6)
reviewer2.rate_student(student2, 'Git', 9)
reviewer2.rate_student(student2, 'Git', 8)

##################### def ###############################
student_all = [student1, student2]

def all_students_grades(student, course):
    students_lst = []
    for student in student_all:
        if course in student.grades:
            students_lst += student.grades[course]
        else:
            return 'Что то пошло не так'
        result = sum(students_lst) / len(students_lst)
    return round(result, 1)

lecturer_all = [lecturer1, lecturer2]

def all_lecturer_grades(lecturer, course):
    lecturer_lst = []
    for lecturer in lecturer_all:
        if course in lecturer.course_grades:
            lecturer_lst += lecturer.course_grades[course]
        else:
            return 'Что то пошло не так'
        result = sum(lecturer_lst) / len(lecturer_lst)
    return round(result, 1)


##################### print ###########################
print('Студент:')
print(student1.__str__())
print(student2.__str__())
print('Лектор:')
print(lecturer1.__str__())
print(lecturer2.__str__())
print('Проверяющий:')
print(reviewer1.__str__())
print(reviewer2.__str__())

print(f"Средняя оценка у студентов по Python: {all_students_grades(student_all, 'Python')}")
print(f"Средняя оценка у студентов по Git: {all_students_grades(student_all, 'Git')}")

print(f"Средняя оценка у лекторов за Python: {all_lecturer_grades(lecturer_all, 'Python')}")
print(f"Средняя оценка у лекторов за Git: {all_lecturer_grades(lecturer_all, 'Git')}")

print(student1.__lt__(student2))
print(lecturer1.__lt__(lecturer2))