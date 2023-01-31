class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.home_work_grades = []

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        aver = sum(self.home_work_grades) / len(self.home_work_grades)
        return aver

    def __str__(self):
        rez = self.average_rating()
        return f"Student \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {rez} \n" \
               f"Курсы в процессе изучения: {(', '.join(self.courses_attached))} \nЗавершенные курсы: {self.finished_courses}"

    def __lt__(self, other):
        print('Сравниваем у двух студентов оценки за домашнее задание')
        return self.home_work_grades == other.home_work_grades


class Mentor:
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.courses_attached = []


class Lecturer(Mentor, Student):
    grades = {}

    def average_rating(self):
        aver = sum(self.grades[self.course]) / len(self.grades[self.course])
        return aver

    def __str__(self):
        rez = self.average_rating()
        return f"lecturer \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {rez} "


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
        return f"Reviewer \nИмя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.home_work_grades = [8, 10, 7, 6, 10]
best_student.courses_attached = ['Python', 'Git']
best_student.finished_courses = "Введение в программирование"
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy', "Python")
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Danil', 'Vandam', "Python")
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades = {'Python': [10, 9, 10, 10, 9]}

cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)
cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)

student1 = Student('Masha', 'Lov', "woman")
student1.grades = {'Python': [5, 10, 4, 2, 10], 'javascript': [9, 10, 9, 4, 10]}
student1.home_work_grades = [10, 7, 8, 9, 10]
student1.finished_courses = ['Основы программирования']
student1.courses_attached = ['Python', 'javascript']

student2 = Student('Dima', 'Denisov', "man")
student2.home_work_grades = [10, 9, 10, 9, 10]
student2.grades = {'Python': [6, 9, 7, 8, 10], 'javascript': [8, 10, 8, 8, 9]}
student2.finished_courses = ['Основы программирования', 'Git', 'C++']
student2.courses_attached = ['Python', 'javascript', ]

mentor1 = Mentor('Oleg', 'Ym', 'Git')
mentor2 = Mentor('Maks', 'Dom', 'Python')

lecturer1 = Lecturer('Vlad', 'Stashevski', 'Python')
lecturer1.grades = {'Python': [10, 9, 10, 8, 10], 'Git': [10, 9, 10, 10, 9]}
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer('Vladimir', 'klyar', 'Git')
lecturer2.grades = {'Python': [10, 8, 10, 10, 8], 'Git': [10, 5, 10, 10, 7]}
lecturer2.courses_attached += ["Git"]

reviewer1 = Reviewer('Yarik', 'Bull', 'Python')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Sasha', 'Klinton', 'Python')
reviewer2.courses_attached += ['Python']

l_students = [student1, student2, best_student]
courses = ['Python', 'Git']


def average_mark_all_students_for_course(l_students, course='Python'):
    list_average_rating = []
    for student in l_students:
        s = student.average_rating()
        list_average_rating.append(s)
    average_mark = round((sum(list_average_rating) / len(l_students)), 1)
    print(f"Средняя оценка за домашнее задание всех студентов: {average_mark} на курсе {course}")


average_mark_all_students_for_course(l_students)

l_lecturers = [lecturer1, lecturer2]


def average_mark_all_lecturer_for_course(l_lecturers, course='Python'):
    list_average_rating = []
    for lecturer in l_lecturers:
        all_grades_one_lecturer = lecturer.grades[f"{course}"]
        sum_all_grades_one_lecturer = sum(all_grades_one_lecturer)
        average_mark_lecture = sum_all_grades_one_lecturer / len(all_grades_one_lecturer)
        list_average_rating.append(average_mark_lecture)
    average_mark_all_lecturer = sum(list_average_rating) / len(l_lecturers)
    print(f"Средняя оценка всех лекторов: {average_mark_all_lecturer} в рамках курса {course}")


average_mark_all_lecturer_for_course(l_lecturers, course='Python')
