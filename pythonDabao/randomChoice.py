import tkinter as tk  # 导入tkinter库，用于创建图形用户界面
import random  # 导入random库，用于生成随机数
from tkinter import ttk  # 从tkinter库中导入ttk模块，用于创建更现代化的控件

class RandomNamePicker(tk.Tk):  # 定义RandomNamePicker类，继承自tkinter的Tk类
    def __init__(self):  # 类的初始化方法
        super().__init__()  # 调用父类的初始化方法

        self.title("Random Name Picker")  # 设置窗口标题
        self.geometry("450x250")  # 设置窗口大小

        # 定义名字列表，存储待抽选的名字
        self.all_names = ["小明", "小芳", "小红", "小黑", "小白", "小灰", "小二", "小三", "小四", "小小"]
        self.remaining_names = self.all_names.copy()  # 创建一个剩余名字的列表，用于存储尚未被点过名的学生

        # 创建标签，显示提示信息，设置字体为楷体
        self.label = ttk.Label(self, text="点击开始按钮\n随机抽选今天的幸运学员", font=("KaiTi", 20), anchor="center", justify="center")
        self.label.pack(pady=20, expand=True, fill="both")  # 将标签添加到窗口中

        # 创建标签，显示恭喜信息，设置字体为楷体
        self.congratulations = ttk.Label(self, text="", font=("KaiTi", 18), anchor="center", justify="center")
        self.congratulations.pack(pady=10, expand=True, fill="both")  # 将恭喜信息标签添加到窗口中

        # 创建按钮，用于开始和停止滚动，设置字体为楷体
        self.start_stop_button = ttk.Button(self, text="开始", command=self.toggle, style='Big.TButton')
        self.start_stop_button.pack(pady=10)  # 将按钮添加到窗口中

        self.is_rolling = False  # 定义一个布尔变量，表示是否正在滚动
        self.rolling = None  # 定义一个变量，用于存储滚动事件

        # 创建一个样式对象，用于自定义控件的样式
        style = ttk.Style()
        style.configure('Big.TButton', font=('KaiTi', 20))  # 为开始/停止按钮设置字体样式为楷体

    def toggle(self):  # 定义一个方法，用于在滚动和停止状态之间切换
        if not self.remaining_names:  # 如果剩余名字列表为空（所有人都已被点过名）
            # 更新恭喜信息标签，显示提示信息
            self.congratulations.config(text="所有人都已被点过名！")
            return  # 直接返回，不执行后续代码

        if self.is_rolling:  # 如果当前正在滚动
            self.stop()  # 调用stop方法，停止滚动
        else:  # 如果当前未在滚动
            self.start()  # 调用start方法，开始滚动

    def start(self):  # 定义开始滚动的方法
        self.is_rolling = True  # 将滚动状态设置为True
        self.start_stop_button.config(text="停止")  # 将按钮文本更改为“停止”
        self.congratulations.config(text="")  # 清空恭喜信息标签的文本
        self.roll()  # 调用roll方法，开始滚动名字

    def roll(self):  # 定义滚动名字的方法
        if self.is_rolling:  # 如果当前正在滚动
            # 更改标签文本为剩余名字列表中的一个随机名字
            self.label.config(text=random.choice(self.remaining_names))
            # 使用after()方法定时调用roll()方法，实现名字的连续滚动
            self.after(100, self.roll)

    def stop(self):  # 定义停止滚动的方法
        self.is_rolling = False  # 将滚动状态设置为False
        self.start_stop_button.config(text="开始")  # 将按钮文本更改为“开始”
        chosen_name = self.label['text']  # 获取当前显示的名字
        # 显示恭喜信息，包括被选中的名字
        self.congratulations.config(text=f"恭喜 {chosen_name} 被选中！")
        self.remaining_names.remove(chosen_name)  # 将选中的名字从剩余名字列表中移除

if __name__ == "__main__":  # 判断是否是主模块
    app = RandomNamePicker()  # 创建RandomNamePicker类的实例
    app.mainloop()  # 运行tkinter的事件循环，启动程序
