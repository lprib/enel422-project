import numpy as np
import matplotlib.pyplot as plt
from constants import *
from baseband_tx import *
from eye_diagram import *

EbN0 = 10
Es = 5
N0 = Es / (20**(EbN0 / 10))


def noisy_channel(modulated):
    variance = N0 / (2 * UPSAMPLE_AMOUNT) * np.dot(RRCOS_FILTER, RCOS_FILTER)
    noise = np.random.normal(0, np.sqrt(variance), modulated.shape)
    return modulated + noise


def plot_awgn_eye_diagram():
    plot_eye_diagram_with_channel(noisy_channel, 20)


if __name__ == "__main__":
    plot_awgn_eye_diagram()
    plt.show()
