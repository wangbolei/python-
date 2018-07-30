class A():
    name = "dana"
    age = 18

    # 注意say的写法,参数有一个self
    def say(self):
        self.name = "aaa"
        self.age = 200


# 此时A称为类实例
print(A.name)
print(A.age)

print("*" * 2000)

print(id(A.name))
print(id(A.age))

print("*" * 2000)

a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))



print(A.name)
print(A.age)

print("*" * 2000)

print(id(A.name))
print(id(A.age))

print("*" * 2000)

a = A()
print(A.__dict__)
print(a.__dict__)
a.name = "yaona"
a.age = 16
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("*" * 2000)

class Student():
    name = "dana"
    age = 18

    # 注意say的写法,参数有一个self
    def say(self):
        self.name = "aaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

yueyue = Student()
yueyue.say()


print("*" * 2000)

class Teacher():
    name = "dana"
    age = 19

    def say(self):
        self.name = "yaona"
        self.age = 16
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print("Hello ,nice to see you again")

t = Teacher()
t.say()
# 调用绑定类函数使用类命
Teacher.sayAgain()



print("*" * 2000)


#关于self的案例

class A():
    name = "wangbolei"
    age = 22

    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = 90

a = A()
#此时,系统会默认把a作为第一个参数传入函数
a.say()

#此时,self被a替换
A.say(a)
#同样可以把A作为参数传入
A.say(A)

#此时,传入的是类实例B,因为B具有name和age属性,所以不会报错
A.say(B)
#以上代码,利用了鸭子模型<只要长得一样,不管是不是同一个东西>

print("*" * 2000)



class Person():
    # name是公有的成员
    name = "wangbolei"
    # __age是私有成员
    __age = 22

p = Person()
#name是公有变量
print(p.name)
print(p._Person__age)
