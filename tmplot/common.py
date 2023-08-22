import argparse
import sys
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any, List, Tuple

import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt

from .logger import generate_logger

LOGGER = generate_logger(__name__)


@dataclass
class CommonPlotter(metaclass=ABCMeta):
    args: argparse.ArgumentParser
    xdata: List[Any] = None
    ydata: List[Any] = None
    fig_width: float = None
    fig_height: float = None
    xmin: float = None
    xmax: float = None
    ymin: float = None
    ymax: float = None
    fig: matplotlib.figure.Figure = None
    ax: matplotlib.axes._axes.Axes = None

    def data_parse(self, dim: int) -> Tuple[List[Any]]:
        if self.args.file == "-":
            LOGGER.info("pipe input")
            return self.data_parse_from_pipe(dim)
        else:
            LOGGER.info("file input")
            return self.data_parse_from_file(dim)

    def data_parse_from_pipe(self, dim: int) -> Tuple[List[Any]]:
        xdata = []
        ydata = []
        for line in sys.stdin:
            line = line.rstrip()
            a = line.split(self.args.split)
            # xdata
            if self.args.xtype == "float":
                xdata.append(float(a[0]))
            elif self.args.xtype == "int":
                xdata.append(int(a[0]))
            elif self.args.xtype == "str":
                xdata.append(str(a[0]))
            if dim >= 2:
                # ydata
                if self.args.ytype == "float":
                    ydata.append(float(a[1]))
                elif self.args.ytype == "int":
                    ydata.append(int(a[1]))
                elif self.args.ytype == "str":
                    ydata.append(str(a[1]))
        return (xdata, ydata)

    def data_parse_from_file(self, dim: int) -> Tuple[List[Any]]:
        xdata = []
        ydata = []
        with open(self.args.file) as ref:
            for line in ref:
                line = line.rstrip()
                a = line.split(self.args.split)
                # xdata
                if self.args.xtype == "float":
                    xdata.append(float(a[0]))
                elif self.args.xtype == "int":
                    xdata.append(int(a[0]))
                elif self.args.xtype == "str":
                    xdata.append(str(a[0]))
            if dim >= 2:
                # ydata
                if self.args.ytype == "float":
                    ydata.append(float(a[1]))
                elif self.args.ytype == "int":
                    ydata.append(int(a[1]))
                elif self.args.ytype == "str":
                    ydata.append(str(a[1]))
        return (xdata, ydata)

    def range_parse(self, lim_range) -> Tuple[float, float]:
        lim_range = lim_range.lstrip("[").rstrip("]")
        lim_range = lim_range.split(":")
        min_ = float(lim_range[0])
        max_ = float(lim_range[1])
        return min_, max_

    @abstractmethod
    def run(self) -> None:
        pass

    def __post_init__(self) -> None:
        # data
        if sys.argv[1] in ["plot", "scatter"]:
            dim = 2
        elif sys.argv[1] in ["hist"]:
            dim = 1
        self.xdata, self.ydata = self.data_parse(dim=dim)
        LOGGER.info("data_parse finished")
        # figsize
        self.fig_width, self.fig_height = self.range_parse(self.args.figsize)
        LOGGER.info(f"figsize: {self.fig_width}x{self.fig_height}")
        # range
        if self.args.xlim is not None:
            self.xmin, self.xmax = self.range_parse(self.args.xlim)
            LOGGER.info(f"xlim: {self.xmin}:{self.xmax}")
        if self.args.ylim is not None:
            self.ymin, self.ymax = self.range_parse(self.args.ylim)
            LOGGER.info(f"ylim: {self.ymin}:{self.ymay}")
        # figure prepare
        self.fig, self.ax = plt.subplots(figsize=(self.fig_width, self.fig_height))
        self.ax.set_xlabel(self.args.xlabel)
        self.ax.set_ylabel(self.args.ylabel)
        self.ax.set_title(self.args.title)
        # seaborn
        if self.args.seaborn_off is False:
            sns.set(style="darkgrid", palette="muted", color_codes=True)
        # grid
        if self.args.grid_off is False:
            self.ax.grid()
        # plot range
        if self.args.xlim is not None:
            self.ax.xlim(self.xmin, self.xmax)
        if self.args.ylim is not None:
            self.ax.ylim(self.ymin, self.ymax)

    def save(self) -> None:
        self.fig.tight_layout()
        if self.args.out is not None:
            plt.savefig(self.args.out)
            LOGGER.info(f"figure name is {self.args.out}")
        else:
            LOGGER.info(f"No file output. Will use additional window")
            plt.show()
