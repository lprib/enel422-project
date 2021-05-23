import matplotlib
import matplotlib.pyplot as plt

from pulse_shape_psd import plot_rcos_psd
from baseband_tx import plot_baseband_tx
from eye_diagram import plot_eye_diagram
from awgn import plot_awgn_eye_diagram
from baseband_rx import plot_error_rate, plot_error_rate_log


def setup_latex_plotting():
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
        "text.usetex": True,
        "pgf.rcfonts": False,
    })


def save_plot(function):
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
