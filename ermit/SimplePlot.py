import matplotlib.pyplot as plt


class SimplPlot:
    def __init__(self, title):
        self.title = title
        self.signal_x = None
        self.signal_y = None
        self.signal_label = None
        self.signal_color = None
        self.result_x = None
        self.result_y = None
        self.result_label = None
        self.result_color = None

    def set_signal(self, x: list, y: list, label: str, color: str):
        self.signal_x = x
        self.signal_y = y
        self.signal_label = label
        self.signal_color = color

    def set_result(self, x: list, y: list, label: str, color: str):
        self.result_x = x
        self.result_y = y
        self.result_label = label
        self.result_color = color

    def show(self):
        fig, ax = plt.subplots()
        ax.plot(self.signal_x, self.signal_y, color='tab:' + self.signal_color, label=self.signal_label)
        ax.plot(self.result_x, self.result_y, color='tab:' + self.result_color, label=self.result_label)
        fig.legend(loc='upper left')
        plt.grid()
        plt.show()
