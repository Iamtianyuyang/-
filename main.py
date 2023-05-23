import tkinter as tk
from tkinter import filedialog
import os
import threading
import numpy as np
import RickerWave
import DataProcess
import Render

def open_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        print("Selected file:", file_path)
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        entry.config(state='readonly')

def update_values():
    global head, rear, x, y,freq
    head = float(entry_head.get())
    rear = float(entry_rear.get())
    x = float(entry_x.get())
    y = float(entry_y.get())
    freq = float(entry_freq.get())
    print("Updated values: head={}, rear={}, x={}, y={} ,频率={}".format(head, rear, x, y,freq))

def process_and_render_AI():
    file_path = entry.get()
    canvas.delete("all")
    if file_path:
        filepath = file_path
        ricker = RickerWave.RickerWave(freq=freq, head=head, hear=rear, dt=0.001,x=x, y=y,root=root,canvas=canvas)
        t, RKW = ricker.generate()
        data = np.loadtxt(filepath)
        processdata = DataProcess.DataProcess(filepath=filepath)
        ProcessedData = processdata.Process()

        AI = Render.Render(ProcessedData, data, x=x, y=y,canvas=canvas,root = root)
        AI.renderAI()

def process_and_render_RF():
    file_path = entry.get()
    canvas.delete("all")
    if file_path:
        filepath = file_path
        ricker = RickerWave.RickerWave(freq=freq, head=head, hear=rear, dt=0.001,x=x, y=y,root=root,canvas=canvas)
        t, RKW = ricker.generate()
        data = np.loadtxt(filepath)
        processdata = DataProcess.DataProcess(filepath=filepath)
        ProcessedData = processdata.Process()

        AI = Render.Render(ProcessedData, data, x=x, y=y,canvas=canvas,root = root)
        AI.renderRF()

def process_and_render_CV():
    file_path = entry.get()
    canvas.delete("all")
    if file_path:
        filepath = file_path
        ricker = RickerWave.RickerWave(freq=freq, head=head, hear=rear, dt=0.001,x=x, y=y,root=root,canvas=canvas)
        t, RKW = ricker.generate()
        data = np.loadtxt(filepath)
        processdata = DataProcess.DataProcess(filepath=filepath)
        ProcessedData = processdata.Process()

        AI = Render.Render(ProcessedData, data, x=x, y=y,canvas=canvas,root = root)
        AI.convole(RkW=RKW)
        AI.renderCV(RkW=RKW)
def process_and_render_SoundWave():
    file_path = entry.get()
    canvas.delete("all")
    if file_path:
        filepath = file_path
        ricker = RickerWave.RickerWave(freq=freq, head=head, hear=rear, dt=0.001,x=x, y=y,root=root,canvas=canvas)
        t, RKW = ricker.generate()
        data = np.loadtxt(filepath)
        processdata = DataProcess.DataProcess(filepath=filepath)
        ProcessedData = processdata.Process()

        AI = Render.Render(ProcessedData, data, x=x, y=y,canvas=canvas,root = root)
        AI.renderSoundWave()

def process_and_render_RickerWave():
    file_path = entry.get()
    canvas.delete("all")
    if file_path:
        filepath = file_path
        # 绘制Ricker Wave
        ricker = RickerWave.RickerWave(freq=freq, head=head, hear=rear, dt=0.001,x=x, y=y,root=root,canvas=canvas)
        ricker.plot()



def process_and_render_Combined():
    file_path = entry.get()
    canvas.delete("all")
    if file_path:
        filepath = file_path
        ricker = RickerWave.RickerWave(freq=freq, head=head, hear=rear, dt=0.001,x=x, y=y,root=root,canvas=canvas)
        t, RKW = ricker.generate()
        data = np.loadtxt(filepath)
        processdata = DataProcess.DataProcess(filepath=filepath)
        ProcessedData = processdata.Process()

        AI = Render.Render(ProcessedData, data, x=x, y=y,canvas=canvas,root = root,)
        AI.renderCombined(RkW=RKW,freq=freq, head=head,hear = rear, dt=0.001)
def clearcanvas():
    canvas.delete("all")
    root.update()
if __name__ == "__main__":
    global root
    root = tk.Tk()
    root.title("Tianyuyang的作业")
    head = -0.05
    rear = 0.2
    x = 2.5
    y = 10
    freq = 50
    global canvas
    canvas = tk.Canvas(root, width=200, height=400)
    canvas.grid(row=0, column=3, rowspan=9, padx=5, pady=5)

    label = tk.Label(root, text="请选择文件:")
    label.grid(row=0, column=0, padx=5, pady=5)


    entry = tk.Entry(root)
    entry.grid(row=0, column=1, padx=5, pady=5)
    entry.bind('<Button-1>', lambda e: open_file())
    label_head = tk.Label(root, text="开始时间:")
    label_head.grid(row=1, column=0, padx=5, pady=5)
    entry_head = tk.Entry(root)
    entry_head.insert(0, str(head))
    entry_head.grid(row=1, column=1, padx=5, pady=5)

    label_rear = tk.Label(root, text="结束时间:")
    label_rear.grid(row=2, column=0, padx=5, pady=5)
    entry_rear = tk.Entry(root)
    entry_rear.insert(0, str(rear))
    entry_rear.grid(row=2, column=1, padx=5, pady=5)

    label_x = tk.Label(root, text="分辨率x:")
    label_x.grid(row=3, column=0, padx=5, pady=5)
    entry_x = tk.Entry(root)
    entry_x.insert(0, str(x))
    entry_x.grid(row=3, column=1, padx=5, pady=5)

    label_freq = tk.Label(root, text="频率HZ:")
    label_freq.grid(row=5, column=0, padx=5, pady=5)
    entry_freq = tk.Entry(root)
    entry_freq.insert(0, str(freq))
    entry_freq.grid(row=5, column=1, padx=5, pady=5)


    label_y = tk.Label(root, text="y:")
    label_y.grid(row=4, column=0, padx=5, pady=5)
    entry_y = tk.Entry(root)
    entry_y.insert(0, str(y))
    entry_y.grid(row=4, column=1, padx=5, pady=5)
    # 创建一个按钮用于更新变量的值
    button_update = tk.Button(root, text="更新变量", command=update_values)
    button_update.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    # 创建按钮分别控制绘制图像
    button_AI = tk.Button(root, text="绘制声阻抗曲线图像", command=process_and_render_AI)
    button_AI.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    button_RF = tk.Button(root, text="绘制反射系数曲线图像", command=process_and_render_RF)
    button_RF.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    button_CV = tk.Button(root, text="绘制合成地震记录图像", command=process_and_render_CV)
    button_CV.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    button_CV = tk.Button(root, text="绘制子波图像", command=process_and_render_RickerWave)
    button_CV.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    button_CV = tk.Button(root, text="绘制声波曲线图像", command=process_and_render_SoundWave)
    button_CV.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

    button_CV = tk.Button(root, text="绘制全部图像", command=process_and_render_Combined)
    button_CV.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

    button_CV = tk.Button(root, text="刷新", command=clearcanvas)
    button_CV.grid(row=13, column=0, columnspan=2, padx=5, pady=5)



    root.mainloop()
