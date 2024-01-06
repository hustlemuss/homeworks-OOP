class Student:
    def __init__(self, name, surname, gender):
        self.name, self.surname, self.gender = name, surname, gender
        self.finished_courses, self.courses_in_progress, self.grades = [], [], {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, grade):
        if isinstance(lecturer, Lecturer) and lecturer in self.courses_in_progress:
            course = lecturer.courses_attached[0]
            self.grades.setdefault(course, []).append(grade)

    def __str__(self):
        avg_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        in_progress, finished = ', '.join(self.courses_in_progress), ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n' \
               f'Курсы в процессе изучения: {in_progress}\nЗавершенные курсы: {finished}'


class Mentor:
    def __init__(self, name, surname):
        self.name, self.surname = name, surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def rate_lecture(self, student, grade):
        if isinstance(student, Student) and self.courses_attached and self.courses_attached[0] in student.courses_in_progress:
            self.grades.append(grade)

    def __str__(self):
        avg_grade = sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_hw_grade(students, course_name):
    total_grades, total_assignments = 0, 0
    for student in students:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name])
            total_assignments += len(student.grades[course_name])
    return total_grades / total_assignments if total_assignments > 0 else 0


def average_lecture_grade(lecturers, course_name):
    total_grades, total_lecturers = 0, 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades += sum(lecturer.grades[course_name])
            total_lecturers += 1
    return total_grades / total_lecturers if total_lecturers > 0 else 0



student1, student2 = Student('Ruoy', 'Eman', 'your_gender'), Student('John', 'Doe', 'male')
student1.courses_in_progress, student2.courses_in_progress = ['Python'], ['Python', 'Git']
student1.add_courses('Введение в программирование')

lecturer1, lecturer2 = Lecturer('Some', 'Buddy'), Lecturer('Another', 'Person')
lecturer1.courses_attached, lecturer2.courses_attached = ['Python'], ['Python']

reviewer1, reviewer2 = Reviewer('Jack', 'Mathers'), Reviewer('Piter', 'Parker')
reviewer1.courses_attached, reviewer2.courses_attached = ['Python'], ['Python']


lecturer1.rate_lecture(student1, 9)
lecturer1.rate_lecture(student2, 8)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)


print(student1, "\n")
print(student2, "\n")
print(lecturer1, "\n")
print(lecturer2, "\n")
print(reviewer1, "\n")
print(reviewer2, "\n")


course_name = 'Python'

avg_hw_grade_result = average_hw_grade([student1, student2], course_name)
avg_lecture_grade_result = average_lecture_grade([lecturer1, lecturer2], course_name)

print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw_grade_result:.2f}")
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture_grade_result:.2f}")

print(student1)

