import argparse
import sys
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any, List, Tuple
import numpy as np

import matplotlib
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
    ax1: matplotlib.axes._axes.Axes = None
    ax2: matplotlib.axes._axes.Axes = None
    ax3: matplotlib.axes._axes.Axes = None

    @abstractmethod
    def run(self) -> None:
        pass

    def __post_init__(self) -> None:
        # data
        self.data = data_parse(self.args.file, self.args.delimiter)
        if sys.argv[1] in ["plot", "scatter"]:
            assert self.data.shape[1] == 3, "data shape must be (N, 3)"
        LOGGER.info("data_parse finished")

        # figsize
        self.fig_width, self.fig_height = range_parse(self.args.figsize)
        LOGGER.info(f"figsize: {self.fig_width}x{self.fig_height}")
        self.fig = plt.figure(figsize=(self.fig_width, self.fig_height))
        grid = plt.GridSpec(10, 10, wspace=0)
        self.ax1 = fig.add_subplot(grid[0:, 0:2]) # left hand histogram
        self.ax2 = fig.add_subplot(grid[0:, 2:8]) # main 2data plot
        self.ax3 = fig.add_subplot(grid[0:, 8:])  # right hand histogram
        self.ax2.set_xlabel(self.args.xlabel)
        self.ax2.set_ylabel(self.args.ylabel)
        self.ax2.set_title(self.args.title)
        self.ax1.set_xlabel("Ratio [%]")
        self.ax3.set_xlabel("Ratio [%]")

        # make_hist1
        for t in [1, 2]:
            hist_data = []
            for data in self.data:
                for data in data[:, t]:
                    hist_data.append(data)
            ydata, xdata = make_hist(hist_data, args.binsize)

            if t == 1:
                self.ax1.plot(ydata, xdata)
            if t == 2:
                self.ax2.plot(ydata, xdata)

        # grid
        if self.args.grid_off is False:
            self.ax1.grid()
            self.ax2.grid()
            self.ax3.grid()
            LOGGER.info("grid on")

        # plot range
        if self.args.xlim is not None:
            self.xmin, self.xmax = range_parse(self.args.xlim)
            LOGGER.info(f"xlim: {self.xmin}:{self.xmax}")
            self.ax2.set_xlim(self.xmin, self.xmax)
        if self.args.ylim is not None:
            self.ymin, self.ymax = range_parse(self.args.ylim)
            LOGGER.info(f"ylim: {self.ymin}:{self.ymax}")
            self.ax1.set_ylim(self.ymin, self.ymax)
            self.ax2.set_ylim(self.ymin, self.ymax)
            self.ax3.set_ylim(self.ymin, self.ymax)

    def save(self) -> None:
        self.fig.tight_layout()
        if self.args.out is not None:
            plt.savefig(self.args.out)
            LOGGER.info(f"figure name is {self.args.out}")
        else:
            LOGGER.info("No file output. Will use additional window")
            plt.show()
