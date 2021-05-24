import matplotlib.pyplot as plt

import awgn
import baseband_rx
import baseband_tx
import constants
import eye_diagram
import pulse_shape_psd


def run_module(module):
    print(f"Running module {module.__name__}")
    module.main()


def main():
    run_module(awgn)
    run_module(baseband_rx)
    run_module(baseband_tx)
    run_module(constants)
    run_module(eye_diagram)
    run_module(pulse_shape_psd)


if __name__ == "__main__":
    main()
    plt.show()
