import argparse
import sys

from .cat.hist import Hist as CatHist
from .cat.plot import Plot as CatPlot
from .cat.scatter import Scatter as CatScatter
from .logger import generate_logger
from .single.hist import Hist as SingleHist
from .single.plot import Plot as SinglePlot
from .single.scatter import Scatter as SingleScatter
from .twin.plot import Plot as TwinPlot
from .twin.scatter import Scatter as TwinScatter

LOGGER = generate_logger(__name__)


def add_common_figure_option(args: argparse.ArgumentParser):
    args.add_argument("-xl", "--xlabel", type=str, default="")
    args.add_argument("-yl", "--ylabel", type=str, default="")
    args.add_argument("--xlim", type=str, help="ex. [10:150]")
    args.add_argument("--ylim", type=str, help="ex. [10:150]")
    args.add_argument("--grid-off", action="store_true")
    args.add_argument("-t", "--title", type=str, default=" ")
    args.add_argument(
        "-o",
        "--out",
        type=str,
        help="If you don't set this, \
                tmplot will open the additional plot window (e.g. Xquartz)",
    )
    args.add_argument(
        "--figsize", type=str, default="[6.4:4.8]", help="[default: [6.4:4.8]]"
    )


def add_hist_option(args: argparse.ArgumentParser):
    args.add_argument("--binsize", type=int, default=100, help="[default: 100]")


def add_single_data_option(args: argparse.ArgumentParser):
    args.add_argument(
        "-f",
        "--file",
        type=str,
        required=True,
        help='input file must be space speparate file. \
                If you want to use pipe input, use "-f -"',
    )
    args.add_argument("-d", "--delimiter", type=str, help="[default: ' ']")


def add_multi_data_option(args: argparse.ArgumentParser):
    args.add_argument(
        "-f",
        "--files",
        type=str,
        required=True,
        nargs="*",
        help='input several data file, but "-f -" cannot be used',
    )
    args.add_argument("-d", "--delimiter", type=str, help="[default: ' ']")


def cli() -> None:
    # make parser
    parser = argparse.ArgumentParser(
        description=(
            "tmplot: One liner Plotter \
                    that supports file and pipe input for quick visualization"
        )
    )

    # subcommands
    subparsers = parser.add_subparsers()

    # plot
    # receive one (N, 2) data from args or stdin
    # plot timeseries
    parser_plot = subparsers.add_parser("plot", help="plot mode")
    add_single_data_option(parser_plot)
    add_common_figure_option(parser_plot)

    # scatter
    # receive one (N, 2) data from args or stdin
    parser_scatter = subparsers.add_parser("scatter", help="scatter mode")
    add_single_data_option(parser_scatter)
    add_common_figure_option(parser_scatter)

    # hist
    # receive one (N, 1) data from args or stdin
    parser_hist = subparsers.add_parser("hist", help="hist mode")
    add_single_data_option(parser_hist)
    add_common_figure_option(parser_hist)
    add_hist_option(parser_hist)

    # cat
    # receive some data from args, not stdin
    # plot at once
    parser_cat = subparsers.add_parser("cat", help="cat mode")
    parser_cat_sub = parser_cat.add_subparsers()

    # cat-plot
    # receive some data which have (N, 2) format
    parser_cat_plot = parser_cat_sub.add_parser("plot", help="cat plot mode")
    add_multi_data_option(parser_cat_plot)
    add_common_figure_option(parser_cat_plot)
    add_hist_option(parser_cat_plot)

    # cat-scatter
    # receive some data which have (N, 2) format
    parser_cat_scatter = parser_cat_sub.add_parser("scatter", help="cat scatter mode")
    add_multi_data_option(parser_cat_scatter)
    add_common_figure_option(parser_cat_scatter)
    add_hist_option(parser_cat_scatter)

    # cat-hist
    # receive some data which have (N, 1) format
    parser_cat_hist = parser_cat_sub.add_parser("hist", help="cat hist mode")
    add_multi_data_option(parser_cat_hist)
    add_common_figure_option(parser_cat_hist)
    add_hist_option(parser_cat_hist)

    # twin
    # receive one (N, 3) data from args or stdin
    # plot timeseries with histogram distribution
    parser_twin = subparsers.add_parser("twin", help="twin mode")
    parser_twin_sub = parser_twin.add_subparsers()

    # twin plot
    parser_twin_plot = parser_twin_sub.add_parser("plot", help="twin plot")
    add_single_data_option(parser_twin_plot)
    add_common_figure_option(parser_twin_plot)
    add_hist_option(parser_twin_plot)

    # twin scatter
    parser_twin_scatter = parser_twin_sub.add_parser("scatter", help="twin plot")
    add_single_data_option(parser_twin_scatter)
    add_common_figure_option(parser_twin_scatter)
    add_hist_option(parser_twin_scatter)

    args = parser.parse_args()

    # error
    if len(sys.argv) == 1:
        LOGGER.error(f"Use {sys.argv[0]} -h")
        exit(1)

    # subcommand process
    LOGGER.info(f"{sys.argv[1]} called")
    if sys.argv[1] == "plot":
        plot = SinglePlot(args=args)
        plot.run()
    elif sys.argv[1] == "scatter":
        scatter = SingleScatter(args=args)
        scatter.run()
    elif sys.argv[1] == "hist":
        hist = SingleHist(args=args)
        hist.run()
    elif sys.argv[1] == "cat":
        if len(sys.argv) == 2:
            LOGGER.error(f"Use {sys.argv[0]} cat -h")
            exit(1)
        if sys.argv[2] == "plot":
            cat = CatPlot(args=args)
            cat.run()
        if sys.argv[2] == "scatter":
            cat = CatScatter(args=args)
            cat.run()
        if sys.argv[2] == "hist":
            cat = CatHist(args=args)
            cat.run()
    elif sys.argv[1] == "twin":
        if len(sys.argv) == 2:
            LOGGER.error(f"Use {sys.argv[0]} twin -h")
            exit(1)
        if sys.argv[2] == "plot":
            cat = TwinPlot(args=args)
            cat.run()
        if sys.argv[2] == "scatter":
            cat = TwinScatter(args=args)
            cat.run()
    LOGGER.info(f"{sys.argv[1]} finished")
