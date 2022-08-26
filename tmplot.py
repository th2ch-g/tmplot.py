

"""
name = tmplot.py
repository = https://github.com/th2ch-g/tmplot.py
author = ["th 2022"]
version = 0.1.0 (under development)
LICENSE = MIT-LICENSE
"""



import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns



def arg_parser():

    # parser object
    parser = argparse.ArgumentParser(description = 'Plotter that supports file and pipe input for quick description')

    # mode option
    parser.add_argument("mode", help = "choose plot mode from {plot, scatter, hist, bar}", choices = ['plot', 'scatter', 'hist', 'bar', 'violin', 'box', 'circle'])

    # basic data option
    parser.add_argument("-x", "--xdata", type = str, required = True, help = "x_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-x - \"")
    parser.add_argument("-y", "--ydata", type = str, required = True, help = "y_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-y - \"")
    parser.add_argument("-s", "--split", type = str, default = " ", help = "Target character for data division [default: <SPACE>]")
    parser.add_argument("--xtype", type = str, default = "float", help = "Input x data type specification [default: float]", choices = ["float", "int", "str"])
    parser.add_argument("--ytype", type = str, default = "float", help = "Input y data type specification [default: float]", choices = ["float", "int", "str"])

    # plot option
    parser.add_argument("--xlim", type = str, help = "plotting range. input data type must be INT or FLOAT (Ex. --xlim \"[10:100]\") [default: not set]")
    parser.add_argument("--ylim", type = str, help = "plotting range. input data type must be INT or FLOAT (Ex. --ylim \"[10:100]\") [default: not set]")
    parser.add_argument("--xlog", action = "store_true", help = "Flag whether the x-axis should be log scaled")
    parser.add_argument("--ylog", action = "store_true", help = "Flag whether the y-axis should be log scaled")
    parser.add_argument("--xline", type = float, help = "Draw a vertical line where the x-axis is (Ex. --xline 10) [default: not set]")
    parser.add_argument("--yline", type = float, help = "Draw a vertical line where the y-axis is (Ex. --yline 10) [default: not set]")

    # input data option
    parser.add_argument("--xnorm", action = "store_true", help = "Flag whether inputed x data normalization")
    parser.add_argument("--ynorm", action = "store_true", help = "Flag whether inputed y data normalization")
    parser.add_argument("--xstand", action = "store_true", help = "Flag whether inputed x data standardization")
    parser.add_argument("--ystand", action = "store_true", help = "Flag whether inputed y data standardization")

    # output picture option
    parser.add_argument("--prefix", type = str, default = "out", help = "output picture file prefix. [default: out]")
    parser.add_argument("--xlabel", type = str, default = "x", help = "output picture xlabel. [default: x]")
    parser.add_argument("--ylabel", type = str, default = "y", help = "output picture ylabel. [default: y] [default(hist): Frequency]")
    parser.add_argument("--title", type = str, default = " ", help = "output picture title. [default: <NONE>]")
    parser.add_argument("--jpg", action = 'store_true', help = "Flag whether JPG output is performed. [default: <PREFIX>.png]")
    parser.add_argument("--transparent", action = "store_true", help = "Flag whether make the background of the output image transparent")
    parser.add_argument("--seaborn-off", action = "store_true", help = "Flag whether seaborn theme off")

    # mode specific option
    parser.add_argument("--hist-bins", type = int, default = 0, help = "number of bins in hist mode. [default: auto]")
    parser.add_argument("--hist-cumulative", action = "store_true", help = "Flag whether plot cumulative ratio with histogram")
    parser.add_argument("--hist-peak-highlight", action = "store_true", help = "Flag whether the major peaks of the histogram are drawn as vertical lines")


    return parser.parse_args()



def mode_plot(args):

    # data input
    xdata, ydata = data_parser(args)

    # data modify
    if args.xnorm == True:
        xdata = data_normalize(xdata)
    if args.xstand == True:
        xdata = data_standardize(xdata)
    if args.ynorm == True:
        ydata = data_normalize(ydata)
    if args.ystand == True:
        ydata = data_standardize(ydata)


    # figure prepare
    sns.set(style = "darkgrid", palette = "muted", color_codes = True)
    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()
    plt.grid()

    # data plotting range
    if args.xlim != None:
        xmin, xmax = range_parser(args.xlim)
        plt.xlim(xmin, xmax)
    if args.ylim != None:
        ymin, ymax = range_parser(args.ylim)
        plt.ylim(ymin, ymax)

    ax.plot(xdata, ydata)

    fig.tight_layout()

    # save figure
    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")


def mode_scatter(args):

    # data input
    xdata, ydata = data_parser(args)

    # data modify
    if args.xnorm == True:
        xdata = data_normalize(xdata)
    if args.xstand == True:
        xdata = data_standardize(xdata)
    if args.ynorm == True:
        ydata = data_normalize(ydata)
    if args.ystand == True:
        ydata = data_standardize(ydata)


    # figure prepare
    sns.set(style = "darkgrid", palette = "muted", color_codes = True)
    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()
    plt.grid()

    # data plotting range
    if args.xlim != None:
        xmin, xmax = range_parser(args.xlim)
        plt.xlim(xmin, xmax)
    if args.ylim != None:
        ymin, ymax = range_parser(args.ylim)
        plt.ylim(ymin, ymax)


    ax.scatter(xdata, ydata)

    fig.tight_layout()

    # save figure
    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")


def mode_hist(args):

    # data input
    if args.ydata != "-":
        print("[WARN] If hist mode, inputed ydata is ignored", file = sys.stdout)
    if args.xdata == "-":
        data = data_from_pipe1()
    else:
        data = data_from_file(args.xdata)

    # data modify
    if args.xnorm == True:
        data = data_normalize(data)
    if args.xstand == True:
        data = data_standardize(data)

    # bin num
    if args.hist_bins == 0:
        # Sturges' rule.
        #bins = int(np.log2(len(data))) + 1
        # Freedman–Diaconis' choice
        q75, q25 = np.percentile(data, [75 ,25])
        iqr = q75 - q25
        bins = int(2 * iqr / pow(len(data), 1/3))
    else:
        bins = args.hist_bins
    print("[INFO] number of bins : {}".format(bins), file = sys.stdout)


    # figure prepare
    sns.set(style = "darkgrid", palette = "muted", color_codes = True)

    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    if args.ylabel == "y":
        ylabel = "Frequency"
    else:
        ylabel = args.ylabel
    ax.set_ylabel(ylabel)
    ax.set_title(args.title)
    ax.grid()
    plt.grid()

    # data plotting range
    if args.xlim != None:
        xmin, xmax = range_parser(args.xlim)
        plt.xlim(xmin, xmax)
    if args.ylim != None:
        ymin, ymax = range_parser(args.ylim)
        plt.ylim(ymin, ymax)

    # hist plot
    if args.hist_cumulative:
        print("[INFO] plot with cumulative ratio plot", file = sys.stdout)
        n, bins, patches = ax.hist(data, alpha = 0.7, bins = bins, label = ylabel)
        y2 = np.add.accumulate(n) / n.sum()
        x2 = np.convolve(bins, np.ones(2) / 2, mode="same")[1:]
        ax2 = ax.twinx()
        lines = ax2.plot(x2, y2, ls = '--', color = 'r', marker = 'o', label = 'cumulative ratio')
        plt.legend(handles=[patches[0], lines[0]])
    else:
        print("[INFO] histogram only", file = sys.stdout)
        ax.hist(data, bins = bins)

    fig.tight_layout()

    # save figure
    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")


"""
def mode_bar(args):
    pass
"""


def range_parser(lim_range):

    print("[INFO] plotting range parser is called", file = sys.stdout)

    if ":" not in lim_range:
        print("[ERROR] plotting range parser error, not include \":\"", file = sys.stderr)
        print("[ERROR] For --xlim or --ylim, use \"[10:100]\" as example", file = sys.stderr)
        sys.exit(1)


    if "[" not in lim_range:
        print("[ERROR] plotting range parser error, not include \"[\"", file = sys.stderr)
        print("[ERROR] For --xlim or --ylim, use \"[10:100]\" as example", file = sys.stderr)
        sys.exit(1)


    if "]" not in lim_range:
        print("[ERROR] plotting range parser error, not include \"]\"", file = sys.stderr)
        print("[ERROR] For --xlim or --ylim, use \"[10:100]\" as example", file = sys.stderr)
        sys.exit(1)


    lim_range = lim_range.lstrip("[").rstrip("]")
    lim_range_list = lim_range.split(":")

    if len(lim_range_list) != 2:
        print("[ERROR] plotting range parser error, seems to be not include number", file = sys.stderr)
        print("[ERROR] For --xlim or --ylim, use \"[10:100]\" as example", file = sys.stderr)
        sys.exit(1)

    min_ = float(lim_range_list[0])
    max_ = float(lim_range_list[1].split("\n")[0])

    if min_ >= max_ :
        print("[ERROR] range must be A < B, if input string is \"[A:B]\"", file = sys.stderr)
        print("[ERROR] For --xlim or --ylim, use \"[10:100]\" as example", file = sys.stderr)
        sys.exit(1)

    print("[INFO] plotting range parser normally terminated", file = sys.stdout)

    return min_, max_


def data_from_pipe2(args):

    print("[INFO] 2 pipe input execute", file = sys.stdout)
    xdata = []
    ydata = []

    for line in sys.stdin:

        if args.split == "\\t":
            a = line.split("\t")
        else:
            a = line.split(args.split)

        try:
            xdata.append(float(a[0]))
            ydata.append(float(a[1].split("\n")[0]))
        except:
            print("[ERROR] check target split character is correct or number of data inputed", file = sys.stderr)
            sys.exit(1)

    return xdata, ydata


def data_from_pipe1():

    print("[INFO] 1 pipe input execute", file = sys.stdout)

    data = []

    for line in sys.stdin:

        data.append(float(line.split("\n")[0]))

    return data


def data_from_file(file):

    print("[INFO] file input execute", file = sys.stdout)

    data = []

    with open(file) as ref:

        for line in ref:

            data.append(float(line.split("\n")[0]))

    return data



def data_parser(args):

    if args.xdata == "-" and args.ydata == "-":
        return data_from_pipe2(args)

    elif args.xdata == "-" and args.ydata != "-":
        return data_from_pipe1(), data_from_file(args.ydata)

    elif args.xdata == "-" and args.ydata != "-":
        return data_from_file(args.xdata), data_from_pipe1()

    else:
        return data_from_file(args.xdata), data_from_file(args.ydata)


"""
def data_cut(data, min_, max_):

   return list(filter(lambda x: min_ <= x <= max_, data))

def data_together(data, multiply):

    return list(map(lambda x: x * multiply, data))
"""


def data_normalize(data):

    print("[INFO] data_normalize is called", file = sys.stdout)

    max_ = np.max(data)
    min_ = np.min(data)

    return list(map(lambda x: (x - min_) / (max_ - min_), data))


def data_standardize(data):

    print("[INFO] data_standardize is called", file = sys.stdout)

    mean_ = np.mean(data)
    std_ = np.std(data)

    return list(map(lambda x: (x - mean_) / std_, data))





if __name__ == "__main__":

    # arg
    args = arg_parser()

    # mode
    if args.mode == "plot":
        print("[INFO] plot mode ", file = sys.stdout)
        mode_plot(args)

    elif args.mode == "scatter":
        print("[INFO] scatter mode", file = sys.stdout)
        mode_scatter(args)

    elif args.mode == "hist":
        print("[INFO] hist mode", file = sys.stdout)
        mode_hist(args)

    elif args.mode == "bar":
        print("[INFO] bar mode", file = sys.stdout)
        mode_bar(args)
    else :
        print("[ERROR] mode name error", file = sys.stderr)
        sys.exit(1)

    print("[INFO] tmplot.py done", file = sys.stdout)

