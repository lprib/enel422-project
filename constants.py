import math
import commpy.filters
import numpy as np
import matplotlib.pyplot as plt

BIT_RATE = 1_500_000
BITS_PER_SYMBOL = 2
SYMBOL_RATE = BIT_RATE / BITS_PER_SYMBOL
SYMBOL_PERIOD = 1 / SYMBOL_RATE

UPSAMPLE_AMOUNT = 64
UPSAMPLED_SAMPLE_RATE = SYMBOL_RATE * UPSAMPLE_AMOUNT
UPSAMPLED_SAMPLE_PERIOD = 1 / UPSAMPLED_SAMPLE_RATE

PAM4_SYMBOLS = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1): +1,
    (1, 0): +3
}

PAM4_REVERSE_SYMBOLS = {
    -3: (0, 0),
    -1: (0, 1),
    +1: (1, 1),
    +3: (1, 0)
}

RRCOS_FILTER = commpy.filters.rrcosfilter(
    4*UPSAMPLE_AMOUNT,
    1,
    SYMBOL_PERIOD,
    UPSAMPLED_SAMPLE_RATE
)[1] / math.sqrt(UPSAMPLE_AMOUNT)

RCOS_FILTER = np.convolve(RRCOS_FILTER, RRCOS_FILTER, mode="same")

if __name__ == "__main__":
    plt.figure()
    plt.plot(RRCOS_FILTER)
    plt.grid()
    plt.title("Root raised cosine impulse")

    plt.figure()
    plt.plot(RCOS_FILTER)
    plt.grid()
    plt.title("Raised cosine impulse")

    plt.show()
