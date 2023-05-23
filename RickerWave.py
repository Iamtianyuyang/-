import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class RickerWave:
    def __init__(self, freq, head , hear, dt,x,y,root,canvas):
        self.freq = freq
        self.head = head
        self.hear = hear
        self.dt = dt
        self.x = x
        self.y = y
        self.root = root
        self.canvas =canvas
    def generate(self):
        t = np.arange(self.head, self.hear, self.dt)
        wave = (1 - 2 * (np.pi ** 2) * (self.freq ** 2) * (t ** 2)) * np.exp(
            -(np.pi ** 2) * (self.freq ** 2) * (t ** 2))
        return t, wave

    def plot(self):
        t, wave = self.generate()
        fig=plt.figure(figsize=(self.x, self.y))
        plt.plot(wave, t)
        plt.xlabel('Amplitude')
        plt.ylabel('Time')
        plt.title('Ricker Wave')
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
        self.toolbar.grid(row=1, column=12, rowspan=40, padx=5, pady=5)
