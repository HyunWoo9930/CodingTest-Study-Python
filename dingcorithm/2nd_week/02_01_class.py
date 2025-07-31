class Person:
    def __init__(self, name_param):
        self.name = name_param
        print('hihi iam created')

    def talk(self):
        print("안녕하세요 저는 ", self.name, "입니다")


person01 = Person('유재석')
person01.talk()
person02 = Person('박명수')
person02.talk()
