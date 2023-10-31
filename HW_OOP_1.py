class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_rating(self):
        grade = []
        for key, value in self.grades.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_rating}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self._avg_rating() < other._avg_rating()

    def __gt__(self, other):
        return self._avg_rating() > other._avg_rating()

    def __eq__(self, other):
        return self._avg_rating() == other._avg_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

#    def _avg_grade(self, lecture, grade):
    def _avg_rating(self):
        grade = []
        for key, value in self.grades.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_rating}"

    def __lt__(self, other):
        return self._avg_rating() < other._avg_rating()

    def __gt__(self, other):
        return self._avg_rating() > other._avg_rating()

    def __eq__(self, other):
        return self._avg_rating() == other._avg_rating()

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def avg_student_grade(student, course):
    grades_sum = 0
    length = 0
    for one_student in student:
        if one_student.grades == ['course']:
            grades_sum += sum(one_student.grades['course'])
            length += len(one_student.grades['course'])
        else:
            return 'Нет такого курса'
    return f'Средний бал за курс {course}: {round(grades_sum / length, 2)}'

def avg_lecturer_grade(lecturer, course):
    grades_sum = 0
    length = 0
    for one_lecturer in lecturer:
        if one_lecturer.grades == ['course']:
            grades_sum += sum(one_lecturer.grades['course'])
            length += len(one_lecturer.grades['course'])
        else:
            return 'Нет такого курса'
    return f'Средний бал за курс {course}: {round(grades_sum / length, 2)}'


student_1 = Student('Ruoy', 'Eman', 'man')
student_2 = Student('Artem', 'Smit', 'woman')
lecturer_1 = Lecturer('Kryak', 'Bidan')
lecturer_2 = Lecturer('Barac', 'Obama')
reviewer_1 = Reviewer('Stiv', 'Jobs')
reviewer_2 = Reviewer('Stiv', 'Voznik')


student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Git', 6)

student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_2.rate_lecturer(lecturer_2, 'Git', 7)


print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)


