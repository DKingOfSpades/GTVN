# everything related to deciding classes and school schedule
init -100 python:
    # string problem, text of the problem to ask
    # string[] answer_list, list of all posible answers to chose for player
    # int answer_idx, index of the right answer
    # float worth, dictates the percentage of grade this test is, ex: 0.025 = 2.5%
    class Question:
        def __init__(self, problem, answer_list, answer_idx, worth = 0.0):
            self.problem = problem
            self.answer_list = answer_list
            self.answer_idx = answer_idx
            self.worth = worth


    class Course:
        # string name, name of the class, ex: ENGL 1001, CS 1301, etc
        # string day_format, days class takes place, ex: MWF or TTh
        # string period, time period of the class, ex: Morning, Noon, Evening, Night
        # string location, location of the class
        # Question[] question_list, list of questions for tests
        # int[] test_day_list, day of each question for test in question_list, must be >0, unique, increasing, and same length as question_list
        # int grade, out of 100, grade for the class
        # float progress, pecentage of class completed so far, 1.0 = 100%
        def __init__(self, name, day_format, period, location, question_list, test_day_list, grade = 100, progress = 0.0):
            self.name = name
            self.day_format = day_format
            self.period = period
            self.location = location
            self.question_list = question_list
            self.test_day_list = test_day_list
            self.grade = grade
            self.progress = progress
            self.question_list_idx = 0 # to keep track of the next question to ask

        def test():
            self.question_list_idx+=1
            # renpy.show()



label faset_random_schedule:
    $ schedule = []
    $ day_period = [["MWF", "Morning"], ["MWF", "Noon"], ["MWF", "Evening"], ["TR", "Morning"], ["TR", "Noon"], ["TR", "Evening"]]
    $ renpy.random.shuffle(day_period)

    $ eng = day_period.pop()
    $ eng_qlist = []
    $ eng_qlist.append(Question("What do you think is the origin of the term \"magistrate's patronage?\"", ["I", "Minamoto no Yoshitsune", "You made up the term"], 1, worth = 1.0))
    $ first_engl_class = Course("ENGL 1101 English Composition", eng[0], eng[1], "Skiles", eng_qlist, [24])
    $ schedule.append(first_engl_class)

    $ math = day_period.pop()
    $ math_qlist = []
    $ math_qlist.append(Question("Is the line extending from A connecting to B or C", ["B", "C"], 1, worth = 1.0))
    $ first_math_class = Course("MATH 1554 Linear Alebra", math[0], math[1], "Howey", math_qlist, [13])
    $ schedule.append(first_math_class)

    $ hist = day_period.pop()
    $ hist_qlist = []
    $ hist_qlist.append(Question("What event did Emperor Nero add to the Olympics so he could participate?", ["Singing", "Dancing", "Javelin", "Chariot Racing"], 0, worth = 1.0))
    $ first_hist_class = Course("HIST 2111 US History to 1877", hist[0], hist[1], "East Architecture", hist_qlist, [14])
    $ schedule.append(first_hist_class)

    $ phys = day_period.pop()
    $ phys_qlist = []
    $ phys_qlist.append(Question("What is the potential energy of an electron when it is far away from the nucleus?", ["Infinite", "100 KJ", "Zero"], 2, worth = 1.0))
    $ first_phys_class = Course("PHYS 2211 Intro Physics I", phys[0], phys[1], "CULC", phys_qlist, [17])
    $ schedule.append(first_phys_class)

    $ chem = day_period.pop()
    $ chem_qlist = []
    $ chem_qlist.append(Question("What is the atomic number of oxygen?", ["1", "2", "8", "69"], 2, worth = 1.0))
    $ first_chem_class = Course("CHEM 1310 General Chemistry", chem[0], chem[1], "Ford EST", chem_qlist, [20])
    $ schedule.append(first_chem_class)

    return
