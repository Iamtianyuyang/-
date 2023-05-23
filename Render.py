import numpy as np
import matplotlib.pyplot as plt
import RickerWave
import matplotlib.gridspec as gridspec
from PIL import Image
from PIL import ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk


class Render:


    def __init__(self,processeddata,origindata,x,y,canvas,root):
        self.data = processeddata
        self.origindata = origindata
        self.x = x
        self.y = y
        self.rendered_image = None
        self.canvas = canvas
        self.root = root
    def get_image(self):
        # 将绘制的图像转换为PIL Image对象
        image = Image.fromarray(self.rendered_image)

        # 根据画板的大小进行缩放
        canvas_width = self.canvas_width
        canvas_height = self.canvas_height
        image = image.resize((canvas_width, canvas_height))

        # 将PIL Image对象转换为Tkinter PhotoImage对象
        photo_image = ImageTk.PhotoImage(image)

        return photo_image
    def AcousticImpedance(self):
        t = []
        AI = []
        for i in range(len(self.data[:])):
            t.append(self.data[i][0])
            AI.append(self.data[i][1]*self.data[i][2])
        return t,AI
    def renderAI(self):
        t,AI = self.AcousticImpedance()
        fig = plt.figure(figsize=(self.x, self.y))
        plt.plot(AI, t)
        plt.xlabel('AcousticImpedance')
        plt.ylabel('Time')
        plt.title('AcousticImpedance')
        plt.gca().invert_yaxis()  # 反转y轴
        plt.gca().xaxis.tick_top()  # x轴移到顶部
        plt.gca().xaxis.set_label_position('top')  # x轴标签移到顶部
        plt.grid(True)
        plt.show()
        self.canvas.delete("all")
        self.root.update()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=40, padx=5, pady=5)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root,pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=0, column=12, rowspan=40, padx=5, pady=5)


    def Reflectance(self):
        t,AI = self.AcousticImpedance()
        RF = []
        for i in range(1,len(self.data[:])):
            RF.append((AI[i]-AI[i-1])/ (AI[i]+AI[i-1]))
        return t, RF
    def renderRF(self):
        t,RF = self.Reflectance()
        fig = plt.figure(figsize=(self.x, self.y))
        plt.plot(RF, t[1:])
        plt.xlabel('Reflectance')
        plt.ylabel('Time')
        plt.title('Reflectance')
        plt.gca().invert_yaxis()  # 反转y轴
        plt.gca().xaxis.tick_top()  # x轴移到顶部
        plt.gca().xaxis.set_label_position('top')  # x轴标签移到顶部
        plt.grid(True)
        plt.show()
        self.canvas.delete("all")
        self.root.update()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=40, padx=5, pady=5)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root,pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=0, column=12, rowspan=40, padx=5, pady=5)



    def convole(self,RkW):
        t,RF =self.Reflectance()
        RF = np.array(RF)
        RkW = np.array(RkW)
        CV = np.convolve(RF,RkW,'same')
        return t,CV
    def renderCV(self,RkW):
        t, CV = self.convole(RkW)
        fig=plt.figure(figsize=(self.x, self.y))
        plt.plot(CV, t[1:])
        plt.xlabel('convole')
        plt.ylabel('Time')
        plt.title('convole')
        plt.gca().invert_yaxis()  # 反转y轴
        plt.gca().xaxis.tick_top()  # x轴移到顶部
        plt.gca().xaxis.set_label_position('top')  # x轴标签移到顶部
        plt.grid(True)
        plt.show()
        self.canvas.delete("all")
        self.root.update()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=40, padx=5, pady=5)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root,pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=0, column=12, rowspan=40, padx=5, pady=5)


    def Origindata(self):
        for i in range(len(self.origindata[:])):
            for j in range(3):
                if (j == 0):
                    self.origindata[i][j] = self.origindata[i][j] / 1000
                elif (j == 1):
                    self.origindata[i][j] = self.origindata[i][j] * 1000
                elif (j == 2):
                    self.origindata[i][j] = self.origindata[i][j] / 304800
        return self.origindata
    def renderSoundWave(self):
        data = self.Origindata()
        t = []
        SW = []
        for i in range(len(self.data[:])):
            t.append(self.data[i][0])
            SW.append(data[i][1])
        fig = plt.figure(figsize=(self.x, self.y))
        plt.plot(SW, t)
        plt.xlabel('SoundWave')
        plt.ylabel('Time')
        plt.title('SoundWave')
        plt.gca().invert_yaxis()  # 反转y轴
        plt.gca().xaxis.tick_top()  # x轴移到顶部
        plt.gca().xaxis.set_label_position('top')  # x轴标签移到顶部
        plt.grid(True)
        plt.show()
        self.canvas.delete("all")
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=40, padx=5, pady=5)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root,pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=0, column=12, rowspan=40, padx=5, pady=5)


    def renderDensity(self):
        data = self.Origindata()
        t = []
        DS = []
        for i in range(len(self.data[:])):
            t.append(self.data[i][0])
            DS.append(data[i][2])
        fig = plt.figure(figsize=(self.x, self.y))
        plt.plot(DS, t)
        plt.xlabel('Density')
        plt.ylabel('Time')
        plt.title('Density')
        plt.gca().invert_yaxis()
        plt.gca().xaxis.tick_top()
        plt.gca().xaxis.set_label_position('top')
        plt.grid(True)
        plt.show()
        self.canvas.delete("all")
        self.root.update()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=40, padx=5, pady=5)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root,pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=0, column=12, rowspan=40, padx=5, pady=5)



    def renderCombined(self, RkW,freq, head, hear, dt):


        fig = plt.figure(figsize=(self.x*5, self.y))
        gs = gridspec.GridSpec(1, 6, figure=fig)
        # 创建RickerWave实例并绘制图像
        ricker = RickerWave.RickerWave(freq, head, hear, dt,self.x, self.y,self.root,self.canvas)

        # 获取RickerWave图像的坐标和波形数据
        t_ricker, wave_ricker = ricker.generate()

        # 绘制RickerWave图
        ax5 = fig.add_subplot(gs[0, 0])
        ax5.plot(wave_ricker, t_ricker)
        ax5.set_xlabel('Amplitude')
        ax5.set_ylabel('Time')

        ax5.invert_yaxis()
        ax5.xaxis.tick_top()
        ax5.xaxis.set_label_position('top')
        ax5.grid(True)
        # 绘制Acoustic Impedance图
        ax1 = fig.add_subplot(gs[0, 1])
        t, AI = self.AcousticImpedance()
        ax1.plot(AI, t)
        ax1.set_xlabel('Acoustic Impedance')
        ax1.set_ylabel('Time')

        ax1.invert_yaxis()
        ax1.xaxis.tick_top()
        ax1.xaxis.set_label_position('top')
        ax1.grid(True)

        # 绘制Reflectance图
        ax2 = fig.add_subplot(gs[0, 2])
        t, RF = self.Reflectance()
        ax2.plot(RF, t[1:])
        ax2.set_xlabel('Reflectance')
        ax2.set_ylabel('Time')

        ax2.invert_yaxis()
        ax2.xaxis.tick_top()
        ax2.xaxis.set_label_position('top')
        ax2.grid(True)

        # 绘制Convolution图
        ax3 = fig.add_subplot(gs[0, 3])
        t, CV = self.convole(RkW)
        ax3.plot(CV, t[1:])
        ax3.set_xlabel('Convolution')
        ax3.set_ylabel('Time')

        ax3.invert_yaxis()
        ax3.xaxis.tick_top()
        ax3.xaxis.set_label_position('top')
        ax3.grid(True)

        # 绘制Density图
        ax4 = fig.add_subplot(gs[0, 4])
        data = self.Origindata()
        t = []
        DS = []
        for i in range(len(self.data[:])):
            t.append(self.data[i][0])
            DS.append(data[i][2])
        ax4.plot(DS, t)
        ax4.set_xlabel('Density')
        ax4.set_ylabel('Time')

        ax4.invert_yaxis()
        ax4.xaxis.tick_top()
        ax4.xaxis.set_label_position('top')
        ax4.grid(True)

        # 绘制SoundWave图
        ax6 = fig.add_subplot(gs[0, 5])
        data = self.Origindata()
        t = []
        SW = []
        for i in range(len(self.data[:])):
            t.append(self.data[i][0])
            SW.append(data[i][1])
        ax6.plot(SW, t)
        ax6.set_xlabel('SoundWave')
        ax6.set_ylabel('Time')

        ax6.invert_yaxis()
        ax6.xaxis.tick_top()
        ax6.xaxis.set_label_position('top')
        ax6.grid(True)

        plt.tight_layout()
        plt.show()
        self.canvas.delete("all")
        self.root.update()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=40, padx=5, pady=5)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root,pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=0, column=12, rowspan=40, padx=5, pady=5)



