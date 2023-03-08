class School:
    # Attribute
    schoolname = 'Mee noi kindergarten school'

    # Constructor
    def __init__(self, subject='Python programming language'):
        print('Show this message when Instance was built')
        self.subject = subject

    # Method

    def hello(self):
        print(f'Good morning, Welcome to {self.schoolname}')

    def teach(self):
        print(f'Subject we\'re open {self.subject}')

class Student(School):
    def __init__(self, fullname=None, grade=None, scores=None, subject=None):
        super().__init__(subject)
        self.fullname = fullname
        self.grade = grade
        self.scores = scores

    def score_check(self):
        if self.scores >= 80:
            print(f'Subject {self.subject} is A')
        elif self.scores >=70:
            print(f'Subject {self.subject} is B')
        elif self.scores >= 60:
            print(f'Subject {self.subject} is C')
        elif self.scores >= 50:
            print(f'Subject {self.subject} is D')
        else:
            print(f'Subject {self.subject} is F')

#Instance
#school01 = School()
#print(school01.schoolname)
#school01.hello()
#school01.teach()
print('================================================================')
student01 = Student('Toyota Tsusho', 3, 75, 'Math')
student01.hello()
print(f'School name: {student01.schoolname}')
print(f'Student name: {student01.fullname}')
print(f'Grade: {student01.grade}')
print(f'Scores: {student01.scores}')
student01.score_check()
print('================================================================')
student02 = Student('Toyota Nexty', 5, 90, 'Python Programming')
print(f'School name: {student02.schoolname}')
print(f'Student name: {student02.fullname}')
print(f'Grade: {student02.grade}')
print(f'Scores: {student02.scores}')
student02.score_check()