import numpy as np
import matplotlib.pyplot as plt

from constants import *


def bits_to_symbols(bits):
    return np.array([PAM4_SYMBOLS[x] for x in (tuple(x) for x in np.split(bits, len(bits) / 2))])


def upsample(symbs, amount, prepend_zeros=True):
    if prepend_zeros:
        upsampled = np.zeros((len(symbs) + 1) * amount)
        upsampled[amount::amount] = symbs
        return upsampled
    else:
        upsampled = np.zeros(len(symbs) * amount)
        upsampled[::amount] = symbs
        return upsampled


def plot_baseband_tx():
    bits = np.array([0, 1, 1, 0, 0, 0, 1, 1, 0, 1])
    symbols = bits_to_symbols(bits)
    deltas = upsample(symbols, UPSAMPLE_AMOUNT)
    modulated = np.convolve(deltas, RCOS_FILTER, mode="same")
    t = np.linspace(0, len(modulated) *
                    UPSAMPLED_SAMPLE_PERIOD, len(modulated))

    fix, ax = plt.subplots()
    ax.plot(t, modulated, "C1")
    ax.stem(t[deltas != 0], symbols, basefmt=" ", use_line_collection=True)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Signal")
    ax.ticklabel_format(style="sci", scilimits=(0, 0))
    ax.legend(labels=["$p(t) \\otimes x(t)$", "$x(t)$"])
    ax.grid()


if __name__ == "__main__":
    plot_baseband_tx()
    plt.show()
