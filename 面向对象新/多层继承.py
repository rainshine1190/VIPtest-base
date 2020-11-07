class Master(object):
    def __init__(self):
        self.kongfu = '[ 五香 ??????]'
    def make_cake(self):
        print(f'??{self.kongfu}??????')
class School(object):
    def __init__(self):
        self.kongfu = '[ 香辣 ??????]'


    def make_cake(self):
        print(f'??{self.kongfu}??????')
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创]'
    def make_cake(self):
        self.__init__()
        print(f'??{self.kongfu}??????')
    # ????????????????????????????????????????
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

xiaoming = Prentice()
xiaoming.make_cake()
xiaoming.make_master_cake()
xiaoming.make_school_cake()
xiaoming.make_cake()