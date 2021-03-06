# -*- coding: utf-8 -*-
from conserial import ConSerial
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
        self.con = ConSerial()
        self.window_ = tk.Tk()
        center_window(self.window_, 600, 450)
        self.window_.title('LLCOM 串口调试工具 - 1.0.0')
        self.window_.grab_set()
        self.body()  # 绘制主体
        self.window_.pack_propagate(True)

    def body(self):
        self.main_text(self.window_).pack(padx=5, pady=5, fill=tk.X)
        self.bottom(self.window_).pack(side=tk.BOTTOM, fill=tk.X)
        self.main_bottom(self.window_).pack(side=tk.BOTTOM, fill=tk.X)
        self.main_mid(self.window_).pack(fill=tk.BOTH, expand=tk.YES)

    def main_text(self, parent):  # 绘制显示文本框

        frame = tk.Frame(parent)

        self.text_show = tk.Text(frame)
        self.text_show.tag_config('warn', foreground='red')
        self.text_show.tag_config('confirm', foreground='green')
        self.text_show.pack(fill=tk.X)
        return frame

    def main_mid(self, parent):

        frame = tk.Frame(parent)
        self.main_mid_1(frame).pack(side=tk.LEFT, padx=5, pady=5)
        self.main_mid_2(frame).pack(side=tk.LEFT, padx=5, pady=5)
        self.main_mid_4(frame).pack(side=tk.RIGHT, padx=5, pady=5)
        self.main_mid_3(frame).pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)

        return frame

    def main_mid_1(self, parent):

        def open_port():  # TODO 连接设备
            port = self.port_cb.get()
            baudrate = int(self.baudrate_cb.get())
            print(f'port: {port}, {type(port)}')
            print(f'baudrate: {baudrate}, {type(baudrate)}')
            if port:
                port = port.split('-')[0].strip()
                baudrate = int(baudrate)
                self.con.open(port, baudrate)
                print(self.con.con.inWaiting())
                self.text_show.insert('end', '连接成功；\n\n', 'confirm')
            else:
                self.text_show.insert('end', '请选择端口；\n\n', 'warn')

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
        frame = tk.Frame(parent)
        self.main_bottom_1(frame).pack(side=tk.LEFT, fill=tk.Y, padx=7, pady=2)
        self.main_bottom_2(frame).pack(side=tk.LEFT, padx=1, pady=1)
        self.main_bottom_3(frame).pack(side=tk.LEFT, padx=5, pady=1, fill=tk.X)
        self.main_bottom_4(frame).pack(side=tk.LEFT, padx=1, pady=1)
        self.main_bottom_5(frame).pack(side=tk.LEFT, padx=5, pady=1, fill=tk.X)
        return frame

    def main_bottom_1(self, parent):

        def refresh_port():  # TODO 刷新串口
            port_list = self.con.get_list()  # 获取串口信息
            self.port_cb['value'] = port_list  # 刷新串口下拉列表
            self.port_cb.set('')
        b = tk.Button(parent, text='刷新串口', font=_font, height=1,
                      width=7, padx=1, pady=1, command=refresh_port)
        return b

    def main_bottom_2(self, parent):

        l = tk.Label(parent, text='串口：', font=('微软雅黑', 10))
        return l

    def main_bottom_3(self, parent):  # 串口下拉框

        port_list = self.con.get_list()  # TODO 获取端口列表
        self.port_cb = ttk.Combobox(parent, value=port_list, width=25)
        return self.port_cb

    def main_bottom_4(self, parent):

        l = tk.Label(parent, text='波特率：', font=('微软雅黑', 10))
        return l

    def main_bottom_5(self, parent):  # 波特率下拉表

        port_list = [9600, 115200]  # TODO 波特率
        self.baudrate_cb = ttk.Combobox(parent, value=port_list)
        self.baudrate_cb.current(1)
        return self.baudrate_cb

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
