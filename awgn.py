import numpy as np
import matplotlib.pyplot as plt

from constants import *
from baseband_tx import *
from eye_diagram import *

SYMBOL_ENERGY_IN_CHANNEL = np.sum(np.square(RRCOS_FILTER))

BIT_ENERGY_IN_CHANNEL = SYMBOL_ENERGY_IN_CHANNEL / np.log2(4)

SYMBOL_ENERGY_AFTER_RX = np.sum(np.square(RCOS_FILTER))

BIT_ENERGY_AFTER_RX = SYMBOL_ENERGY_AFTER_RX / np.log2(4)


def gen_noisy_channel(eb_n0):
    n_0 = 1 / eb_n0 * BIT_ENERGY_IN_CHANNEL
    std_dev = np.sqrt(n_0)

    def noisy_channel(modulated):
        noise = np.random.normal(0, std_dev, modulated.shape)
        return modulated + noise

    return noisy_channel


def plot_awgn_eye_diagram():
    plot_eye_diagram_with_channel(gen_noisy_channel(10), 1)


if __name__ == "__main__":
    plot_awgn_eye_diagram()
    plt.show()
