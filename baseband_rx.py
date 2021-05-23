import numpy as np
import matplotlib.pyplot as plt
import scipy.special

from constants import *
from baseband_tx import *
from eye_diagram import *
from awgn import *


def threshold_detector(val):
    if val > 2:
        return PAM4_REVERSE_SYMBOLS[3]
    elif val <= 2 and val > 0:
        return PAM4_REVERSE_SYMBOLS[1]
    elif val <= 0 and val > -2:
        return PAM4_REVERSE_SYMBOLS[-1]
    elif val <= -2:
        return PAM4_REVERSE_SYMBOLS[-3]


def threshold_detector_opt(val):
    return (val >= 0, val <= 2 and val >= -2)


def demod(modulated):
    bits = []
    for sample in modulated[UPSAMPLE_AMOUNT::UPSAMPLE_AMOUNT]:
        symbol = threshold_detector_opt(sample)
        bits.extend(symbol)
    return bits


def error_rate(tx_bits, eb_n0):
    modulated = get_modulation(tx_bits, gen_noisy_channel(eb_n0))
    rx_bits = demod(modulated)
    return (tx_bits != rx_bits).sum() / len(rx_bits)


def q(n):
    return 0.5 - 0.5 * scipy.special.erf(n / np.sqrt(2))


def theoretical_error(eb_n0):
    return q(np.sqrt(2*eb_n0))


def plot_single_error_rate(eb_n0s):
    tx_bits = np.random.randint(0, 2, 10000)
    error_rates = []
    for eb_n0 in eb_n0s:
        error_rates.append(error_rate(tx_bits, eb_n0))
    log_eb_n0 = 10*np.log10(eb_n0s)
    return plt.plot(eb_n0s, np.array(error_rates)*100, "C0")[0]


def plot_error_rate():
    eb_n0s = np.logspace(0, np.log2(10), 20, base=2)

    measured_error_rate_artist = None
    plt.figure()

    for i in range(5):
        print(f"Estimating error rate, run {i}")
        measured_error_rate_artist = plot_single_error_rate(eb_n0s)

    theoretical_error_rate_artist = plt.plot(
        eb_n0s, [theoretical_error(n)*100 for n in eb_n0s], "C1--")[0]

    plt.xlabel("$\\frac{E_b}{N_0}$ (dB)")
    plt.ylabel("Bit error rate (%)")
    plt.legend([measured_error_rate_artist, theoretical_error_rate_artist], [
               "Measured error rate", "Theoretical error rate"])
    plt.grid()


def plot_error_rate_log():
    plot_error_rate()
    plt.yscale("log")


if __name__ == "__main__":
    plot_error_rate()
    plot_error_rate_log()
    plt.show()
