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

    def rate_lecturer(self, lecturer, grade):
        if isinstance(lecturer, Lecturer) and lecturer in self.courses_in_progress:
            course = lecturer.courses_attached[0]
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {avg_grade:.1f}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
               f'Завершенные курсы: {finished_courses_str}'

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()

    def calculate_average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_assignments = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_assignments if total_assignments > 0 else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def rate_lecture(self, student, grade):
        if isinstance(student, Student) and self.courses_attached and self.courses_attached[0] in student.courses_in_progress:
            self.grades.append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.add_courses('Введение в программирование')

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Another', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer.rate_lecture(best_student, 10)
cool_lecturer.rate_lecture(best_student, 8)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

