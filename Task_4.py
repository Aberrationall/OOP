class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, avg_rate=9.9):
        courses_in_progress_str = "Python, Git"
        finished_courses_str = "Введение в программирование"
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_rate}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")
    
    def __eq__(self, avg_rate):
        return avg_rate == avg_rate
    
    def __ne__(self, avg_rate):
        return avg_rate != avg_rate

    def __lt__(self, avg_rate):
        return avg_rate < avg_rate

    def __gt__(self, avg_rate):
        return avg_rate > avg_rate
    
    def __le__(self, avg_rate):
        return avg_rate <= avg_rate

    def __ge__(self, avg_rate):
        return avg_rate >= avg_rate


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self, avg_rate=9.9):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_rate}"
    
    def __eq__(self, avg_rate):
        return avg_rate == avg_rate

    def __ne__(self, avg_rate):
        return avg_rate != avg_rate
    
    def __lt__(self, avg_rate):
        return avg_rate < avg_rate

    def __gt__(self, avg_rate):
        return avg_rate > avg_rate

    def __le__(self, avg_rate):
        return avg_rate <= avg_rate

    def __ge__(self, avg_rate):
        return avg_rate >= avg_rate


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def avg_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0

def avg_lect_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0
    
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Ruoy2', 'Eman2', 'your_gender')
best_student2.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Some2', 'Buddy2')
cool_reviewer2.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Some2', 'Buddy2')
cool_lecturer2.courses_attached += ['Python']

best_student.rate_lect(cool_lecturer, 'Python', 7)
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 9)

best_student2.rate_lect(cool_lecturer2, 'Python', 10)
best_student2.rate_lect(cool_lecturer2, 'Python', 10)
best_student2.rate_lect(cool_lecturer2, 'Python', 10)


print(best_student.grades)
print(cool_lecturer.grades)
print(cool_reviewer)
print(cool_lecturer)
print(best_student)

print(best_student == 10)
print(best_student != 10)
print(best_student < 10)
print(best_student > 10)
print(best_student <= 10)
print(best_student >= 10)

print(cool_lecturer == 10)
print(cool_lecturer != 10)
print(cool_lecturer < 10)
print(cool_lecturer > 10)
print(cool_lecturer <= 10)
print(cool_lecturer >= 10)


students_list = [best_student, best_student2]
lecturers_list = [cool_lecturer, cool_lecturer2]
print(f"Cредняя оценка за домашнее задания по всем студентам в рамках конкретного курса: {avg_hw_grade(students_list, 'Python')}")
print(f"Средняя оценка за за лекции всех лекторов в рамках курса: {avg_lect_grade(lecturers_list, 'Python')}")