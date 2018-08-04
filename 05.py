#属性案例
#创建Student类,描述学生类
#学生具有Student.name属性
#但name格式并不统一
#可以用增加一个函数,然后自动调用的方法,但很蠢
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)      #自己调用一下,不用修改代码
    def intro(self):
        print("Hello, my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()

s = Student("Bolei Wang", 22)
s.intro()

print("*" * 2000)
############################################################################
#property案例
#定义一个Person类,具有name,age属性
#对于任意输入的姓名,希望都用大写方式保存
#对于年龄,希望内部统一整数保存
# x = property(fget,fset,fdel,doc)
class Person():
    '''
    这是一个人<文档>
    '''
    def fget(self):         #函数名随意
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self.name = "NoName"
    name = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
p1.name = "wangbolei"
print(p1.name)
####################################################################################
print("*"*2000)

#类的内置属性举例
print(Person.__dict__)
print(Person.__doc__)
print(Person.__bases__)
print(Person.__name__)

print("*"*2000)
#init 举例
class A():
    def __init__(self,name = 0):
        print("哈哈,我被调用了")
a = A()
#################################################################################
print("*"*2000)
#__call__举例
class A():
    def __init__(self,name = 0):
        print("哈哈,我被调用了")
    def __call__(self, *args, **kwargs):
        print("我被调用了again")
a = A()
a()

#################################################################################
print("*"*2000)
#__str__举例
class A():
    def __init__(self,name = 0):
        print("哈哈,我被调用了")
    def __call__(self, *args, **kwargs):
        print("我被调用了again")
    def __str__(self):
        return "__str__的例子"
a = A()
a()
print(a)

#################################################################################
print("*"*2000)

#__getattr__  举例

class A():
    name = "NoName"
    age = 22
    def __getattr__(self, name):
        print("没找到")
        print(name)

a = A()
print(a.name)
print(a.addr)

#################################################################################
print("*"*2000)

#__setattr__ 举例
class Person():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性: {0}".format(name))
        #下面语句会出现问题,死循环
        #self.name = value
        #此种情况,为了避免死循环,规定统一调用父类魔法函数
        super().__setattr__(name,value)

p = Person()
print(p.__dict__)
p.age = 18

#################################################################################
print("*"*2000)

#__gt__案例
class Student():
    def __init__(self,name):
        self.name = name
    def __gt__(self, other):
        print("哈哈,{0}会比{1}大吗".format(self, other))
        return self.name > other.name
stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)

#################################################################################
print("*"*2000)

#三种方法的案例
class Person():
    #实例方法
    def eat(self):
        print(self)
        print("eating")
    #类方法
    #类方法的第一个参数,一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("playing")

    #静态方法
    #不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("saying")

yueyue = Person()
#实例方法
yueyue.eat()
#类方法
Person.play()
#静态方法
Person.say()