#coding:utf-8
# __author__ = 'lc'
#在多重继承里面尽可能的不要出现相同的方法名

class Base(object):
    def test(self):
        print("-----base")


class A(Base):
    def test(self):
        print("-----A")

class B(Base):
    def test(self):
        print("-----B")

class C(A,B):
    pass
    # def test(self):
    #     print("-----C")



c = C()
c.test()

print(C.__mro__)