import matplotlib
import matplotlib.pyplot as plt

from pulse_shape_psd import plot_rcos_psd
from baseband_tx import plot_baseband_tx
from eye_diagram import plot_eye_diagram
from awgn import plot_awgn_eye_diagram
from baseband_rx import plot_error_rate, plot_error_rate_log

# Run all plot_x functions and save their output to a .pgf file for importing
# into LaTeX.  Each plot_x will be saved as x.pgf


def setup_latex_plotting():
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
        "text.usetex": True,
        "pgf.rcfonts": False,
    })


def save_plot(function):
    # Strip "plot_" from the start of the function name and use as filename
    func_name = function.__name__
    plot_name = func_name[func_name.index("_") + 1:]

    function()
    plt.savefig(f"latex/plots/{plot_name}.pgf")


if __name__ == "__main__":
    save_plot(plot_rcos_psd)
    save_plot(plot_baseband_tx)
    save_plot(plot_eye_diagram)
    save_plot(plot_awgn_eye_diagram)
    save_plot(plot_error_rate)
    save_plot(plot_error_rate_log)
