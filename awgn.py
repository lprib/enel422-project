import numpy as np
import matplotlib.pyplot as plt

from constants import *
from baseband_tx import *
from eye_diagram import *

# Energies after TX filter but before RX filter
SYMBOL_ENERGY_IN_CHANNEL = np.sum(np.square(RRCOS_FILTER))
BIT_ENERGY_IN_CHANNEL = SYMBOL_ENERGY_IN_CHANNEL / np.log2(4)

# Energies after TX and RX filters
SYMBOL_ENERGY_AFTER_RX = np.sum(np.square(RCOS_FILTER))
BIT_ENERGY_AFTER_RX = SYMBOL_ENERGY_AFTER_RX / np.log2(4)


def gen_noisy_channel(eb_n0):
    """
    A `channel` in this simulation is a function that takes in a modulated
    signal and returns a modulated signal, with arbitrary computation in
    between. This function returns a `channel` (ie. function) that produces AWGN
    with the specified Eb/N0 value.

    The specified Eb/N0 should be in ratio form, not decibels.
    """
    n_0 = 1 / eb_n0 * BIT_ENERGY_IN_CHANNEL
    std_dev = np.sqrt(n_0)

    def noisy_channel(modulated):
        noise = np.random.normal(0, std_dev, modulated.shape)
        return modulated + noise

    return noisy_channel


def plot_awgn_eye_diagram():
    """ Plot an eye diagram with an AWGN channel of Eb/N0 10 """
    plot_eye_diagram_with_channel(gen_noisy_channel(10), 1)


def main():
    plot_awgn_eye_diagram()


if __name__ == "__main__":
    main()
    plt.show()
