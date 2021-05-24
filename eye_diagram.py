import numpy as np
import matplotlib.pyplot as plt

from baseband_tx import *


def int_to_bits(n, width):
    """ Convert an integer to an array of length `width` of {0, 1} """
    bits = []
    for i in reversed(range(width)):
        bits.append((n >> i) & 1)
    return np.array(bits)


def get_modulation(bits, channel_func):
    """
    Given a bitstream `bits`, generate the signal after the reciever's matched
    filter.  `channel_func` is a function that takes a stream of TX modulated
    samples and performs arbitrary transformations to simulate a channel. This
    will be applied after the TX filter and before the RX filter.
    """
    symbols = bits_to_symbols(bits)
    deltas = upsample(symbols, UPSAMPLE_AMOUNT)
    tx_mod = np.convolve(deltas, RRCOS_FILTER, mode="same")
    channel_mod = channel_func(tx_mod)
    rx_mod = np.convolve(channel_mod, RRCOS_FILTER, mode="same")
    return rx_mod


def plot_bit_modulation(ax, bits, channel_func):
    """ Plot the modulation of `bits` over `channel_func` on the axis `ax` """
    modulated = get_modulation(bits, channel_func)
    t = np.linspace(0, len(modulated) *
                    UPSAMPLED_SAMPLE_PERIOD, len(modulated))
    display_slice = slice(UPSAMPLE_AMOUNT, -UPSAMPLE_AMOUNT)
    return ax.plot(t[display_slice], modulated[display_slice], "C0")[0]


def plot_eye_diagram_with_channel(channel_func, repeats=1):
    """
    Generate an eye diagram with the given channel. For random channels,
    `repeats` will replot the data n times drawing over eachother.
    """
    fig, ax = plt.subplots()
    # store a matplotlib `artist` so we can refer to it to color the legend
    eye_artist = None

    for j in range(repeats):
        # Use binary counting to send every possible permutation of 6 bits (3
        # symbols) through the channel to generate a full eye diagram.
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
    """ Plot perfect channel eye diagram """
    # Use lambda x: x (a NO-OP) as the perfect channel
    plot_eye_diagram_with_channel(lambda x: x)


if __name__ == "__main__":
    plot_eye_diagram()
    plt.show()
