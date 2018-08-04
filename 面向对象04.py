class A():
    pass
class B(A):
    pass
print(A.__mro__)

print("*" *2000)
#####################################################################################################
#多继承的实例
#子类可以直接拥有父类的属性和方法,私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("I'm swimming")

class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("I'm flying")

class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("I'm working")

class SuperMan(Person,Bird,Fish):
   def __init__(self,name):
       self.name = name

#单继承例子
class Student(Person):
    def __init__(self,name):
        self.name = name

s = SuperMan("yueyue")
s.fly()
s.swim()

stu = Student("yueyue")
stu.work()

print("*" * 2000)
##################################################################################################
#菱形继承问题
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass


print("*" * 2000)
##################################################################################################

#构造函数例子
class Person():
    #对Person进行实例化的时候
    #姓名要确定
    #年龄要确定
    #地址肯定得有
    def __init__(self):
        self.name = "Noname"
        self.name = 18
        self.address = "Studentwhonheim"
        print("In init func")
p = Person()

print("*" * 2000)
#issubclass

class A():
    pass
class B(A):
    pass
class C():
    pass

print(issubclass(B,A))
print(issubclass(C,A))

a = A()
print(isinstance(a,A))

print("*"*2000)

class A():
    name = "Noname"

a = A()
print(hasattr(a,"name"))

print("*"*2000)

class A():
    pass
print(dir(A))
