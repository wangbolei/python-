#继承的语法
#在python中,任何类都有一个共同的父类叫做object
class Person():
    name = "NoName"
    age = 18
    __score = 0    #考试成绩是秘密,只要自己知道
    _petname = "sec"     #小名是保护的,子类可以用,但不能公用
    def sleep(self):
        print("Sleeping... ...")

#父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    def make_test(self):
        print("attention")

t = Teacher()
print(t.name)
print(Teacher.name)
print(t._petname)
t.sleep()
print(t.teacher_id)
t.make_test()

print("*" * 2000)



class Person():
    name = "NoName"
    age = 18
    __score = 0    #考试成绩是秘密,只要自己知道
    _petname = "sec"     #小名是保护的,子类可以用,但不能公用
    def sleep(self):
        print("Sleeping... ...")
    def work(self):
        print("make some money")

#父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    def make_test(self):
        print("attention")
    def work(self):
        #扩充父类的功能只需要调用父类相同的函数
        super().work()
        Person.work(self)
        self.make_test()


t = Teacher()
t.work()


print("*" * 2000)

# 构造函数的概念
class Dog():
    #__init__就是构造函数
    #每次实例化的时候第一个被调用
    #因为主要工作是进行初始化,所以得名
    def __init__(self):
        print("I am a dog")

kaka = Dog()


print("*" * 2000)
#继承中的构造函数1
class Animal():
    pass
class PaxingAni(Animal):
    pass
class Dog(PaxingAni):
    def __init__(self):
        print("I am a dog")

#实例化的时候,括号内的参数需要跟构造函数的参数相匹配
kaka = Dog()

print("*" * 2000)
#继承中的构造函数2
class Animal():
    def __init__(self):
        print("Animal")
class PaxingAni(Animal):
    def __init__(self):
        print("paxing dongwu")
class Dog(PaxingAni):
    def __init__(self):
        print("I am a dog")

#实例化的时候,括号内的参数需要跟构造函数的参数相匹配
kaka = Dog()

#猫没有构造函数
class Cat(PaxingAni):
    pass

c = Cat()


print("*" * 2000)
#继承中的构造函数3
class Animal():
    def __init__(self):
        print("Animal")
class PaxingAni(Animal):
    def __init__(self,name):
        print("paxing dongwu {0}".format(name))
class Dog(PaxingAni):
    def __init__(self):
        print("I am a dog")

d = Dog()
class Cat(PaxingAni):
    pass
c = Cat("猫可爱")
