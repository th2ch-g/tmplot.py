import argparse
import sys

from ._version import __version__
from .hist import Hist
from .logger import generate_logger
from .plot import Plot
from .scatter import Scatter

LOGGER = generate_logger(__name__)


def add_common_option(args: argparse.ArgumentParser) -> argparse.ArgumentParser:
    # data option
    args.add_argument(
        "-f",
        "--file",
        type=str,
        required=True,
        help='If you want to use pipe input, use "-f -"',
    )
    args.add_argument("-s", "--split", type=str, default=" ", help='[default: " "]')
    args.add_argument(
        "-xt",
        "--xtype",
        type=str,
        default="float",
        choices=["float", "int", "str"],
        help="[default: float]",
    )
    args.add_argument(
        "-yt",
        "--ytype",
        type=str,
        default="float",
        choices=["float", "int", "str"],
        help="[default: float]",
    )

    # draw option
    args.add_argument("-xl", "--xlabel", type=str, default="")
    args.add_argument("-yl", "--ylabel", type=str, default="")

    args.add_argument("--xlim", type=str, help="ex. [10:150]")
    args.add_argument("--ylim", type=str, help="ex. [10:150]")
    args.add_argument("--grid-off", action="store_true")
    args.add_argument("-c", "--color", type=str, help="[default: cornflowerblue]")

    # result option
    args.add_argument("-t", "--title", type=str, default=" ")
    args.add_argument(
        "-o",
        "--out",
        type=str,
        help="If you don't set this, tmplot open the plot window",
    )
    args.add_argument(
        "--figsize", type=str, default="[6.4:4.8]", help="[default: [6.4:4.8]]"
    )

    return args


def cli() -> None:
    # make parser
    parser = argparse.ArgumentParser(
        description=(
            "tmplot: One liner Plotter that supports file and pipe input for quick description"
        )
    )

    parser.add_argument("-V", "--version", action="store_true", help="show version")

    # subcommands
    subparsers = parser.add_subparsers()

    # plot
    parser_plot = subparsers.add_parser("plot", help="plot mode")
    parser_plot = add_common_option(parser_plot)

    # scatter
    parser_scatter = subparsers.add_parser("scatter", help="scatter mode")
    parser_scatter = add_common_option(parser_scatter)

    # hist
    parser_hist = subparsers.add_parser("hist", help="hist mode")
    parser_hist = add_common_option(parser_hist)
    parser_hist.add_argument("-b", "--bin", type=int, help="number of bin-size")

    args = parser.parse_args()

    # error
    if len(sys.argv) == 1:
        LOGGER.error(f"Use {sys.argv[0]} -h")
        exit(1)

    # version
    if args.version is True:
        print(f"{sys.argv[0]}", __version__)
        exit(0)

    # subcommand process
    LOGGER.info(f"{sys.argv[1]} called")
    if sys.argv[1] == "plot":
        plot = Plot(args=args)
        plot.run()
    elif sys.argv[1] == "scatter":
        scatter = Scatter(args=args)
        scatter.run()
    elif sys.argv[1] == "hist":
        hist = Hist(args=args)
        hist.run()
    LOGGER.info(f"{sys.argv[1]} finished")
