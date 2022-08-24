

import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns


def arg_parser():

    parser = argparse.ArgumentParser(description='Plotter that supports file and pipe input for quick description')

    parser.add_argument("mode", help = "chose plot mode from {plot, scatter, hist, bar}", choices = ['plot', 'scatter', 'hist', 'bar'])
    parser.add_argument("-x", "--xdata", type = str, required = True, help = "x_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-x - \"")
    parser.add_argument("-y", "--ydata", type = str, required = True, help = "y_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-y - \"")
    parser.add_argument("-s", "--split", type = str, default = " ", help = "Target character for data division [default: <SPACE>]")
    parser.add_argument("--prefix", type = str, default = "out", help = "output picture file prefix. [default: out]")
    parser.add_argument("--xlabel", type = str, default = "x", help = "output picture xlabel. [default: x]")
    parser.add_argument("--ylabel", type = str, default = "y", help = "output picture ylabel. [default: y] [default(hist): Frequency]")
    parser.add_argument("--title", type = str, default = " ", help = "output picture title. [default: <NONE>]")
    parser.add_argument("--jpg", action = 'store_true', help = "Flag whether JPG output is performed. [default: <PREFIX>.png]")
    parser.add_argument("--hist-bins", type = int, default = 0, help = "number of bins in hist mode. [default: auto]")
    parser.add_argument("--hist-cumulative", action = "store_true", help = "Flag whether plot cumulative ratio with histogram")


    return parser.parse_args()



def mode_plot(args):

    # data input
    xdata, ydata = data_parser(args)

    # figure prepare
    sns.set(style="darkgrid", palette="muted", color_codes=True)
    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()
    plt.grid()

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

    # figure prepare
    sns.set(style="darkgrid", palette="muted", color_codes=True)
    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()
    plt.grid()

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
        print("[WARN] If hist mode, inputed ydata is ignored", file=sys.stdout)
    if args.xdata == "-":
        data = data_from_pipe1()
    else:
        data = data_from_file(args.xdata)

    # bin num
    if args.hist_bins == 0:
        # Sturges' rule.
        bins = int(np.log2(len(data))) + 1
    else:
        bins = args.hist_bins
    print("[INFO] number of bins : {}".format(bins), file=sys.stdout)


    # figure prepare
    sns.set(style="darkgrid", palette="muted", color_codes=True)

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

    if args.hist_cumulative:
        print("[INFO] plot with cumulative ratio plot", file=sys.stdout)
        n, bins, patches = ax.hist(data, alpha = 0.7, bins = bins, label = ylabel)
        y2 = np.add.accumulate(n) / n.sum()
        x2 = np.convolve(bins, np.ones(2) / 2, mode="same")[1:]
        ax2 = ax.twinx()
        lines = ax2.plot(x2, y2, ls='--', color='r', marker='o', label='umulative ratio')
        plt.legend(handles=[patches[0], lines[0]])
    else:
        print("[INFO] histogram only", file=sys.stdout)
        ax.hist(data, bins = bins)

    fig.tight_layout()

    # save figure
    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")


"""
def mode_bar(args):

    # data input
    xdata, ydata = data_parser(args)

    # figure prepare
    sns.set(style="darkgrid", palette="muted", color_codes=True)
    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()
    plt.grid()

    ax.bar(xdata, ydata)

    fig.tight_layout()

    # save figure
    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")

"""


def data_from_pipe2(args):

    print("[INFO] pipe input execute", file=sys.stdout)
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
            print("[ERROR] check target split character is correct or number of data inputed", file=sys.stderr)
            sys.exit(1)

    return xdata, ydata


def data_from_pipe1():

    print("[INFO] pipe input execute", file=sys.stdout)

    data = []

    for line in sys.stdin:

        data.append(float(line.split("\n")[0]))

    return data


def data_from_file(file):

    print("[INFO] file input execute", file=sys.stdout)

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


def data_normalize(data):

    max_ = np.max(data)
    min_ = np.min(data)

    return list(map(lambda x: (x - min_) / (max_ - min_), data))


def data_standardize(data):

    mean_ = np.mean(data)
    std_ = np.std(data)

    return list(map(lambda x: (x - mean_) / std_, data))



def data_together(data, multiply):

    return list(map(lambda x: x * multiply, data))
"""



if __name__ == "__main__":

    # arg
    args = arg_parser()

    print(args)

    # mode
    if args.mode == "plot":
        print("[INFO] plot mode ", file=sys.stdout)
        mode_plot(args)

    elif args.mode == "scatter":
        print("[INFO] scatter mode", file=sys.stdout)
        mode_scatter(args)

    elif args.mode == "hist":
        print("[INFO] hist mode", file=sys.stdout)
        mode_hist(args)

    elif args.mode == "bar":
        print("[INFO] bar mode", file=sys.stdout)
        mode_bar(args)
    else :
        print("[ERROR] mode name error", file=sys.stderr)
        sys.exit(1)

    print("[INFO] tmplot.py done", file=sys.stdout)

