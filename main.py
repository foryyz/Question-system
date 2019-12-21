class Question():

    def __init__(self,questions,answers,choices):
        """初始化"""
        self.questxt = questions    #路径
        self.answtxt = answers
        self.choitxt = choices
        self.grade = 0   #分数
        self.addspeed = 10
        self.sum = 0
        self.q = ""
        self.a = ""
        self.c = ""
        self.qulist = []  #用于提取的列表
        self.anlist = []
        self.chlist = []
        self.qudlis = []  #用于放置的列表
        self.andlis = []
        self.chdlis = []
        self.mistakes = []
        self.index = 0   #索引
        self.active = True  #活动状态
        self.hello = "Hello, welcome to the question answeringsystem.\n"
##        self.hello += "The total score for this test is "+str(self.sum)

    def get_anything(self):
        """打开文件并以列表形式储存起来"""
        with open(self.questxt) as qus:
            self.qulist = qus.readlines()
        with open(self.answtxt) as ans:
            self.anlist = ans.readlines()
        with open(self.choitxt) as chs:
            self.chlist = chs.readlines()
            print("Successfully acquired")

    def show_hello(self):
        """必须先获取 再打印'hello'."""
        self.sum = len(self.qulist)*self.addspeed
        self.hello += "The total score for this test is "+str(self.sum)
        print(self.hello)
        
##    def test(self):

#下面应该在循环中
    def pop_up(self):     
        """弹出列表元素 并使索引加一"""
        self.q = self.qulist.pop(self.index)
        self.a = self.anlist.pop(self.index)
        self.c = self.chlist.pop(self.index)
        self.index + 1
        
    def show_question(self):
        print(self.q)
        print(self.c)
##        print(self.index)  这玩意打印出来一直是0  也不知道为啥
        
    def check_choice(self):
        """获取并核对用户输入 正确加分并储存在d列表中 不正确则把问题储存到mistakes列表中"""
        usput = input('Please enter your choice: ')
        if usput.lower() == self.a.rstrip():
            self.grade += self.addspeed
            self.qudlis.append(self.q)
            self.andlis.append(self.a)
            self.chdlis.append(self.c)
        else:
            self.mistakes.append(self.q)
            self.andlis.append(self.a)
            self.chdlis.append(self.c)

    def check_print_mistake(self):
        """有错误则打印错误  否则打印全部正确的恭喜消息"""
        if self.mistakes:
            print("Your mistakes are : ")
            for self.mistake in self.mistakes:
                print('\t'+self.mistake.rstrip())
        else:
            print("Congratulations! You got all the questions right!\n")
    def show_grade(self):
        """打印总分并退出"""
        print("\nOK! This game is over. And your grade is :" + str(self.grade))
        input("Thanks for your play!  Enter anything to Exit!")
        
