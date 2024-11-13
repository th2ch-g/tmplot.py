import sys
from pathlib import Path
from typing import List, Tuple

import numpy as np

from .logger import generate_logger

LOGGER = generate_logger(__name__)


def data_parse(file: str, delimiter: str) -> np.array:
    if file == "-":
        LOGGER.info("pipe input")
        data = np.loadtxt(sys.stdin)
    else:
        LOGGER.info("file input")
        if Path(file).suffix == "npy":
            data = np.load(file)
        else:
            data = np.loadtxt(file, delimiter=delimiter)
    return data


def data_parse_multi(files: List[str], delimiter: str) -> np.array:
    data = []
    for file in files:
        if file == "-":
            LOGGER.error("file name must not be '-'")
            exit(1)
        data.append(data_parse(file, delimiter))
    data = np.array(data)
    return data


def range_parse(lim_range: str) -> Tuple[float, float]:
    lim_range = lim_range.lstrip("[").rstrip("]")
    lim_range = lim_range.split(":")
    min_ = float(lim_range[0])
    max_ = float(lim_range[1])
    return min_, max_


def make_dist(data: List[float], bin_size: int) -> Tuple[List[float], List[float]]:
    data.sort()
    xdata = []
    ydata = []
    data_size = len(data)
    max_size = max(data)
    min_size = min(data)
    bins = np.linspace(min_size, max_size, bin_size)
    for i in range(len(bins) - 1):
        lower_bound = bins[i]
        upper_bound = bins[i + 1]
        xdata.append(lower_bound)
        ydata.append(
            100 * len([x for x in data if lower_bound <= x < upper_bound]) / data_size
        )
    return (xdata, ydata)
