# everything related to deciding classes and school schedule
init python:
    class course:
        def __init__(self, subject, name, period, hw_list, question_list, grade = 100, progress = 0.0):
            self.subject = subject
            self.name = name
            self.period = period
            self.hw_list = hw_list
            self.question_list = question_list
            self.grade = grade
            self.progress = progress

        def test():
            renpy.show()




label random_schedule:
    default eng_course_list = []
