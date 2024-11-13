import argparse
import sys
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from ..logger import generate_logger
from ..util import data_parse, range_parse

LOGGER = generate_logger(__name__)


@dataclass
class CommonPlotter(metaclass=ABCMeta):
    args: argparse.ArgumentParser
    data: np.array = None
    fig_width: float = None
    fig_height: float = None
    xmin: float = None
    xmax: float = None
    ymin: float = None
    ymax: float = None
    fig: matplotlib.figure.Figure = None
    ax: matplotlib.axes._axes.Axes = None

    @abstractmethod
    def run(self) -> None:
        pass

    def __post_init__(self) -> None:
        # data
        self.data = data_parse(self.args.file, self.args.delimiter)
        if sys.argv[1] in ["plot", "scatter"]:
            assert self.data.shape[1] == 2, "data shape must be (N, 2)"
        elif sys.argv[1] in ["hist"]:
            assert self.data.ndim == 1, "data shape must be (N, )"
        LOGGER.info("data_parse finished")

        # figsize
        self.fig_width, self.fig_height = range_parse(self.args.figsize)
        LOGGER.info(f"figsize: {self.fig_width}x{self.fig_height}")
        self.fig, self.ax = plt.subplots(figsize=(self.fig_width, self.fig_height))
        self.ax.set_xlabel(self.args.xlabel)
        self.ax.set_ylabel(self.args.ylabel)
        self.ax.set_title(self.args.title)

        # grid
        if self.args.grid_off is False:
            self.ax.grid()
            LOGGER.info("grid on")

        # plot range
        if self.args.xlim is not None:
            self.xmin, self.xmax = range_parse(self.args.xlim)
            LOGGER.info(f"xlim: {self.xmin}:{self.xmax}")
            plt.xlim(self.xmin, self.xmax)
        if self.args.ylim is not None:
            self.ymin, self.ymax = range_parse(self.args.ylim)
            LOGGER.info(f"ylim: {self.ymin}:{self.ymax}")
            plt.ylim(self.ymin, self.ymax)

    def save(self) -> None:
        self.fig.tight_layout()
        if self.args.out is not None:
            plt.savefig(self.args.out)
            LOGGER.info(f"figure name is {self.args.out}")
        else:
            LOGGER.info("No file output. Will use additional window")
            plt.show()
