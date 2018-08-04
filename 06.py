#变量的三种用法
class A():
    def __init__(self):
        self.name = "haha"
        self.age =22

a = A()
#属性的三种用法
# 1 赋值
# 2 读取
# 3 删除
a.name = "王博磊"
print(a.name)

print("*"*20000)
#类属性 property
# 应用场景:
# 对变量除了普通的三种操作,还想增加一些附加操作,那么可以通过property完成
class A():
    def __init__(self):
        self.name = "haha"
        self.age =22
    #此功能,对类变量进行读取操作的时候应该执行此函数功能
    def fget(self):
        print("我被读取了")
        return self.name
    #此功能是对变量进行写操作的时候执行此函数
    def fset(self):
        print("我被写入了,但是还可以做好多事情")
        self.name = "图灵学院" + name
    #模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass
    #property的四个参数顺序固定.
    name2 = property(fget,fset,fdel,"这是一个property的例子")

a = A()
print(a.name)
print(a.name2)  #读操作


print("*"*2000)
class Animal():
    def sayHello(self):
       pass
class Dog(Animal):
    def sayHello(self):
        print("闻一下对方的味道")
class Person(Animal):
    def sayHello(self):
        print("Kiss me")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()

print("*"*2000)
#抽象类的实现
import abc
#声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    #定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass
    def sleep(self):
        print("sleeping")

print("*"*2000)
################################################
#自己组装一个类
class A():
    pass
def say(self):
    print("saying... ...")
say(9)
A.say = say
a =A()
a.say()

print("*"*2000)
################################################
#组装类
from types import MethodType

class A():
    pass

def say(self):
    print("saying... ...")

a = A()
a.say = MethodType(say,A)
a.say()

help(MethodType)

print("*"*2000)
################################################

#利用Type造一个类
def say(self):
    print("saying... ...")

def talk(self):
    print("talking... ...")

#用Type创造一个类
A = type("A",(object,),{"class_say":say,"class_talk":talk})

a = A()
a.class_say()
a.class_talk()

print("*"*2000)
################################################

#元类演示

#元类写法是固定的,必须继承自type
#元类命名以MetaClass结尾
class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("哈哈,我是元类")
        attrs['id'] = '000000'
        attrs['addr'] = "陕西省渭南市合阳县"
        return type.__new__(cls, name, bases, attrs)

#元类定义完就可以使用,注意使用写法
class Teacher(object, metaclass=MetaClass):
    pass

t = Teacher()
print(t.id)
print(t.addr)

t.__dict__
