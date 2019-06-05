import datetime
from collections import defaultdict


class HomeworkResult:

    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class DeadlineError(Exception):
    """Thrown if homework was finished after the deadline"""


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):

    def do_homework(self, hw, solution):
        if hw.is_active():
            return HomeworkResult(self, hw, solution)
        raise DeadlineError("You are late!")


class Teacher(Person):
    homework_done = defaultdict()

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    def check_homework(self, hw_result):
        if len(hw_result.solution) > 5:
            self.homework_done[hw_result.homework] = hw_result
            return True
        return False

    @classmethod
    def reset_results(cls, hw=None):
        if hw:
            cls.homework_done.pop(hw)
        else:
            cls.homework_done = defaultdict()


class Homework:

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < self.created + self.deadline


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
