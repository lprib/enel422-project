import numpy as np
import matplotlib.pyplot as plt
from baseband_tx import *


def int_to_bits(n, width):
    bits = []
    for i in reversed(range(width)):
        bits.append((n >> i) & 1)
    return np.array(bits)


def get_modulation(bits, channel_func):
    symbols = bits_to_symbols(bits)
    deltas = upsample(symbols, UPSAMPLE_AMOUNT)
    tx_mod = np.convolve(deltas, RRCOS_FILTER, mode="same")
    channel_mod = channel_func(tx_mod)
    rx_mod = np.convolve(channel_mod, RRCOS_FILTER, mode="same")
    return rx_mod


def plot_bit_modulation(ax, bits, channel_func):
    modulated = get_modulation(bits, channel_func)
    t = np.linspace(0, len(modulated) *
                    UPSAMPLED_SAMPLE_PERIOD, len(modulated))
    return ax.plot(t[UPSAMPLE_AMOUNT:-UPSAMPLE_AMOUNT],
                   modulated[UPSAMPLE_AMOUNT:-UPSAMPLE_AMOUNT], "C0")[0]


def plot_eye_diagram_with_channel(channel_func, repeats=1):
    fig, ax = plt.subplots()
    eye_artist = None
    for j in range(repeats):
        for i in range(2**6):
            eye_artist = plot_bit_modulation(
                ax, int_to_bits(i, 6), channel_func)

    ax.grid()
    ax.ticklabel_format(style="sci", scilimits=(0, 0))
    ideal_sample_x = UPSAMPLED_SAMPLE_PERIOD * (UPSAMPLE_AMOUNT * 2 + 2.5)
    ideal_artist = ax.axvline(ideal_sample_x, color="C1")
    ax.legend([eye_artist, ideal_artist], [
              "Eye diagram", "Ideal sampling instant"], loc="upper right")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Signal")


def plot_eye_diagram():
    plot_eye_diagram_with_channel(lambda x: x)


if __name__ == "__main__":
    plot_eye_diagram()
    plt.show()
