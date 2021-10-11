# -*- coding: utf-8 -*-
import serial
import tkinter as tk
from tkinter import ttk

_font = ('微软雅黑', 8)  # 字体


def center_window(win, width=None, height=None):
    """窗口居中"""
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    if width is None:
        width, height = get_window_size(win)[:2]
    print(f'screen width:{screen_width}, screen height:{screen_height}, '
          f'width: {width}, height: {height}')
    size = '%dx%d+%d+%d' % (width, height, (screen_width - width)/2, (screen_height - height)/3)
    win.geometry(size)


def get_window_size(win, update=True):
    """获取窗体的大小"""
    if update:
        win.update()
    return win.winfo_width(), win.winfo_height(), win.winfo_x(), win.winfo_y()


class LLCom:

    def __init__(self):
        self.window_ = tk.Tk()
        center_window(self.window_, 500, 400)
        self.window_.title('LLCOM 串口调试工具 - 1.0.0')
        self.window_.grab_set()
        self.body()  # 绘制主体

    def body(self):
        self.main_text(self.window_).pack(padx=5, pady=5, fill=tk.X)
        self.main_mid(self.window_).pack(fill=tk.BOTH, expand=tk.YES)
        self.main_bottom(self.window_).pack(fill=tk.X)
        self.bottom(self.window_).pack(fill=tk.X)

    def main_text(self, parent):  # 绘制显示文本框

        frame = tk.Frame(parent)

        self.text_show = tk.Text(frame)
        self.text_show.pack(fill=tk.X)
        return frame

    def main_mid(self, parent):

        frame = tk.Frame(parent, bg='green')
        self.main_mid_1(frame).pack(side=tk.LEFT, padx=5, pady=5)
        self.main_mid_2(frame).pack(side=tk.LEFT, padx=5, pady=5)
        self.main_mid_4(frame).pack(side=tk.RIGHT, padx=5, pady=5)
        self.main_mid_3(frame).pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)

        return frame

    def main_mid_1(self, parent):

        def open_port():  # TODO 连接设备
            self.text_show.insert('end', '连接设备\n\n')

        b = tk.Button(parent, text='打开\n串口', font=_font,
                      height=2, width=5, padx=1, pady=1, command=open_port)
        return b

    def main_mid_2(self, parent):
        frame = tk.Frame(parent)

        b1 = tk.Button(frame, text='清空日志', padx=3, pady=2, bg='whitesmoke')
        b2 = tk.Button(frame, text='更过设置', padx=3, pady=2, bg='whitesmoke')
        b1.pack(side=tk.TOP, fill=tk.X)
        b2.pack(side=tk.TOP, fill=tk.X)
        return frame

    def main_mid_3(self, parent):
        self.text_send = tk.Text(parent)
        return self.text_send

    def main_mid_4(self, parent):

        def write_info():  # TODO 向设备发送命令，并读取设备返回信息
            var = self.text_send.get('1.0', tk.END)
            self.text_show.insert('end', f'{var}\n')

        b = tk.Button(parent, text='发送', font=_font, height=2,
                      width=5, padx=1, pady=1, command=write_info)
        return b

    def main_bottom(self, parent):
        frame = tk.Frame(parent, bg='yellow')
        self.main_bottom_1(frame).pack(side=tk.LEFT, fill=tk.Y, padx=7, pady=7)
        return frame

    def main_bottom_1(self, parent):

        def refresh_port():  # TODO 刷新串口
            self.text_show.insert('end', '刷新串口\n\n')
        b = tk.Button(parent, text='刷新串口', font=_font, height=1,
                      width=7, padx=1, pady=1, command=refresh_port)
        return b

    def bottom(self, parent):
        """窗体最下方留白"""
        frame = tk.Frame(parent, height=10, bg='whitesmoke')
        frame.propagate(True)
        return frame

    def run(self):
        self.window_.mainloop()


if __name__ == "__main__":
    llcom = LLCom()
    llcom.run()
