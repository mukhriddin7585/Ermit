import numpy
import numpy as np

from ermit.SimplePlot import SimplPlot


class Ermit:
    def __init__(self, file):
        self.__run(file)

    @classmethod
    def __run(self, file):
        yf = np.genfromtxt(file)
        xf = numpy.arange(start=1, stop=len(yf) + 1, step=1)
        xv = self.__arange(xf)
        ermit_x = self.__arange(xf)
        ermit_y = self.__ermit_splayn(yf, xf, xv)[0:len(ermit_x)]

        plot = SimplPlot("Ermit splayn")
        plot.set_signal(xf, yf, "Signal", "blue")
        plot.set_result(ermit_x, ermit_y, "Ermit", "orange")
        plot.show()

    @classmethod
    def __arange(self, value):
        r = []
        for x in range(1, len(value) - 2):
            for i in range(1, 100):
                r.append(value[x] + (i * 0.01))
        return r

    @classmethod
    def __ermit_splayn(self, yf, xf, xv):
        sf = []
        for j in range(1, len(xf) - 2):
            for i in range(0, len(xv)):
                if xf[j] <= xv[i] <= xf[j + 1]:
                    t = (xv[i] - xf[j]) / (xf[j + 1] - xf[j])
                    f1 = (pow(1 - t, 2) * (1 + (2 * t)))
                    f2 = pow(t, 2) * (3 - (2 * t))
                    f3 = t * pow((1 - t), 2)
                    f4 = pow(t, 2) * (t - 1)
                    sf.append(f1 * yf[j] + f2 * yf[j + 1] + f3 * (yf[j + 1] - yf[j]) + f4 * (yf[j + 2] - yf[j + 1]))
        return sf
