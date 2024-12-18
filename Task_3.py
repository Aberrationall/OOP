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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lect(cool_lecturer, 'Python', 7)
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 9)

another_lecturer = Lecturer('Another', 'Buddy')
best_student2 = Student('Ruoy2', 'Eman2', 'your_gender')
best_student2.rate_lect(cool_lecturer, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)

