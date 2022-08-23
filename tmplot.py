#!/usr/bin/python3


import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys



def arg_parser():

    parser = argparse.ArgumentParser(description='Plotter that supports file and pipe input for quick description')

    parser.add_argument("mode", help = "chose plot mode from {plot, scatter, hist, bar}", choices = ['plot', 'scatter', 'hist', 'bar'])
    parser.add_argument("-x", "--xdata", type = str, required = True, help = "x_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-x - \"")
    parser.add_argument("-y", "--ydata", type = str, required = True, help = "y_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-y - \"")
    parser.add_argument("-s", "--split", type = str, default = " ", help = "Target character for data division")
    parser.add_argument("--prefix", type = str, default = "out", help = "output picture file prefix")
    parser.add_argument("--xlabel", type = str, default = "xlabel", help = "output picture xlabel")
    parser.add_argument("--ylabel", type = str, default = "ylabel", help = "output picture ylabel")
    parser.add_argument("--title", type = str, default = "title", help = "output picture title")
    parser.add_argument("--jpg", action = 'store_true', help = "Flag whether JPG output is performed")


    return parser.parse_args()



def mode_plot(args):

    xdata, ydata = data_parser(args)

    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()

    ax.plot(xdata, ydata)

    fig.tight_layout()

    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")


def mode_scatter(args):
    xdata, ydata = data_parser(args)

    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()

    ax.scatter(xdata, ydata)

    fig.tight_layout()

    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")

"""
def mode_hist(args):
    xdata, ydata = data_parser(args)

    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()

    ax.hist(xdata, ydata)

    fig.tight_layout()

    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")



def mode_bar(args):
    xdata, ydata = data_parser(args)

    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    ax.set_title(args.title)
    ax.grid()

    ax.bar(xdata, ydata)

    fig.tight_layout()

    if args.jpg :
        plt.savefig(args.prefix + ".jpg")
    else :
        plt.savefig(args.prefix + ".png")
"""


def data_from_pipe2(args):

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
            print("[ERROR] check target split character is correct")
            sys.exit(1)

    return xdata, ydata


def data_from_pipe1():

    data = []

    for line in sys.stdin:

        data.append(float(line.split("\n")[0]))

    return data


def data_from_file(file):

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



if __name__ == "__main__":

    # arg
    args = arg_parser()

    print(args)

    # mode
    if args.mode == "plot":
        print("[INFO] plot mode ")
        mode_plot(args)

    elif args.mode == "scatter":
        print("[INFO] scatter mode")
        mode_scatter(args)

    elif args.mode == "hist":
        print("[INFO] hist mode")
        mode_hist(args)

    elif args.mode == "bar":
        print("[INFO] bar mode")
        mode_bar(args)
    else :
        print("[ERROR] mode name error")
        sys.exit(1)

    print("[INFO] tmplot.py done")

