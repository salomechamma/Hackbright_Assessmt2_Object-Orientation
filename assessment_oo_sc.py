"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   - Abstraction: Ability to use a class and its built-in methods without necessarily understanding how they work and hw they were built
   - Encapsulation: Keep all the specificities of a class or sub-class internally in the class (this include the specific methods, class attribute etc..). They are all located  "next to each other", inside the class definition.
   - Polymorphism: Common variables, methods or objects between all sub-classes of a class. Can have more than one form depending which subclass is used (= same interface for differing underlying forms).

2. What is a class?
A class is a specific data-structure type that can be created in Python.

3. What is an instance attribute?
A class attribute is an attribute common to all instances from that class. In the contrary an instance attribute is proper to the instance, it doesn't share it with the other instances of the class.

4. What is a method? 
A method is a built-in fonction proper to the class 

5. What is an instance in object orientation?
An instance is an object of a class.

6. How is a class attribute different than an instance attribute?
Give an example of when you might use each.
A class attribute is shared by any instances deriving from the class. It will have the same value regardless the instance. The instance attribute "value" will vary dpeending the instance.
For example, if I create the class US_CITIZEN. Each citizen created will be an instance. The class attribute "citizenship" will be set at "US" and will be shared by all instances created via this class.
The instance attribute "age" will differ depending on the citizen.



"""



class Student(object):
    """"Student"""

    def __init__(self, f_name, l_name, address):
        self.first_name = f_name
        self.last_name = l_name
        self.address = address

class Question(object):
    """ Question """

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question + ': ')
        if answer == self.correct_answer:
            return True
        return False
            




class Exam(object):
    """ Exam """

    def __init__(self, name):
        self.name = name
        self.question_list = []

    def add_questions(self, question, correct_answer):
        quest_answ = Question(question, correct_answer)
        self.question_list.append(quest_answ)

    def administer(self):
        score = 0
        if not self.question_list:
            return
        for question in self.question_list:
            round = question.ask_and_evaluate()
            if round == True:
                score += 1
        return float(score)/len(self.question_list) 

def take_test(student,exam):
    score = exam.administer()
    student.score = score


def example(exam_name, question_list, f_name, l_name, address):
    exam1 = Exam(exam_name)
    exam1.question_list = question_list
    student1 = Student(f_name, l_name, address)
    take_test(student1, exam1)
    return student1


class Quizz(Exam):

    def administer(self):
        return (super(Quizz, self).administer()) >= 0.5
        




