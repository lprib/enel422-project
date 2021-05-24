import numpy as np
import matplotlib.pyplot as plt

from constants import *


def rcos_freq_response(f, alpha, bandwidth):
    """ Transcribe peicewise function from lecture notes """
    w = 0.5 * bandwidth
    f1 = w * (1 - alpha)
    f = abs(f)
    if f < f1:
        return 1 / (2 * w)
    elif f >= f1 and f < (2 * w - f1):
        return (1 / (4 * w)) * (1 - np.sin((np.pi * (f - w))/(2 * w - 2 * f1)))
    elif f >= (2 * w - f1):
        return 0


def plot_rcos_psd():
    ALPHA = 1
    DESIRED_BW = 750_000

    f = np.linspace(-1_500_000, 1_500_000, 500)
    Pf = np.array([rcos_freq_response(x, ALPHA, DESIRED_BW) for x in f])
    Pf_scaled = Pf * (5 / SYMBOL_PERIOD)
    fig, ax = plt.subplots()
    ax.set_xlabel("Frequency (Hz)")
    ax.ticklabel_format(style="sci", scilimits=(0, 0))
    ax.plot(f, Pf)
    ax.axvspan(-DESIRED_BW, DESIRED_BW, alpha=0.2, fc="C1")
    ax.legend(labels=["$S_x(f)$", "Bandwidth limit"])
    ax.grid()


def main():
    plot_rcos_psd()


if __name__ == "__main__":
    main()
    plt.show()
