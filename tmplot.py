

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
    parser = argparse.ArgumentParser(description = 'Plotter that supports file and pipe input for quick description',
            formatter_class = argparse.RawTextHelpFormatter)

    # mode option
    parser.add_argument("mode", choices = ['plot', 'scatter', 'hist', 'bar', 'violin', 'box', 'pie', 'empty'],
            help = 'choose plot mode'\
            '\nplot    : connect the dots and draw them.'\
            '\nscatter : NOT connect the dots and draw them.'\
            '\nhist    : draw histogram'\
            '\nbar     : draw bar graph'\
            '\nviolin  : draw violin plot'\
            '\nbox     : draw a box-and-whisker diagram'\
            '\npie     : draw pie charti'\
            '\nempty   : draw NOTHING')

    # basic data option
    parser.add_argument("-x", "--xdata", type = str, required = True,
            help = "x_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-x - \"")
    parser.add_argument("-y", "--ydata", type = str, required = True,
            help = "y_data of 2D-plot. \nSupports FILE name or PIPE input. For pipe input, use \"-y - \"")
    parser.add_argument("-s", "--split", type = str, default = " ",
            help = "Target character for delimiter [default: <SPACE>]")
    parser.add_argument("-xt", "--xtype", type = str, default = "float",
            help = "Input x data type specification [default: float]", choices = ["float", "int", "str"])
    parser.add_argument("-yt", "--ytype", type = str, default = "float",
            help = "Input y data type specification [default: float]", choices = ["float", "int", "str"])

    # plot option
    parser.add_argument("-c", "--color", type = str, default = "cornflowerblue",
            help = "Main plotting color [default: cornflowerblue]\n(See the official matplotlib site for color choices. "\
                    "https://matplotlib.org/stable/gallery/color/named_colors.html)")
    parser.add_argument("-l", "--label", type = str,
            help = "Main plotting label [default: <None>]")
    parser.add_argument("--xlim", type = str,
            help = "plotting range. input data type must be int or float (Ex. --xlim \"[10:100]\") [default: not set]")
    parser.add_argument("--ylim", type = str,
            help = "plotting range. input data type must be int or float (Ex. --ylim \"[10:100]\") [default: not set]")
    parser.add_argument("--xlog", action = "store_true",
            help = "Flag whether the x-axis should be log scaled")
    parser.add_argument("--ylog", action = "store_true",
            help = "Flag whether the y-axis should be log scaled")
    parser.add_argument("--xline", type = str,
            help = "Draw an additional perpendicular lines to the x-axis (Ex. --xline 10) [default: not set]")
    parser.add_argument("--yline", type = str,
            help = "Draw an Additional perpendicular lines to the y-axis (Ex. --yline 10) [default: not set]")
    parser.add_argument("--xline-color", type = str, default = "orange",
            help = "Color of additional perpendicular lines to the x-axis [default: orange]\n(See the official matplotlib site for color choices. "\
                    "https://matplotlib.org/stable/gallery/color/named_colors.html) ")
    parser.add_argument("--yline-color", type = str, default = "tomato",
            help = "Color of additional perpendicular lines to the y-axis [default: tomato]\n(See the official matplotlib site for color choices. "\
                    "https://matplotlib.org/stable/gallery/color/named_colors.html) ")


    # input data option
    parser.add_argument("--xnorm", action = "store_true",
            help = "Flag whether inputed x data normalization"\
                    "If the data type is str, an error will occur")
    parser.add_argument("--ynorm", action = "store_true",
            help = "Flag whether inputed y data normalization"\
                    "If the data type is str, an error will occur")
    parser.add_argument("--xstand", action = "store_true",
            help = "Flag whether inputed x data standardization"\
                    "If the data type is str, an error will occur")
    parser.add_argument("--ystand", action = "store_true",
            help = "Flag whether inputed y data standardization"\
                    "If the data type is str, an error will occur")

    # output picture option
    parser.add_argument("-p", "--prefix", type = str, default = "out",
            help = "output picture file prefix. [default: out]")
    parser.add_argument("-xl", "--xlabel", type = str, default = "x",
            help = "output picture xlabel. [default: x]")
    parser.add_argument("-yl", "--ylabel", type = str, default = "y",
            help = "output picture ylabel. [default: y] [default(hist): Frequency]")
    parser.add_argument("-t", "--title", type = str, default = " ",
            help = "output picture title. [default: <NONE>] If you use \"--title t=p\", title will be the same as prefix")
    parser.add_argument("-j", "--jpg", action = 'store_true', help = "Flag whether JPG output is performed. [default: <PREFIX>.png]")
    parser.add_argument("--transparent", action = "store_true", help = "Flag whether make the background of the output image transparent")
    parser.add_argument("--seaborn-off", action = "store_true", help = "Flag whether seaborn theme off")
    parser.add_argument("--grid-off", action = "store_true", help = "Flag whether turn off grid")


    # mode specific option
    # hist mode option
    parser.add_argument("--hist-bins-width", type = float, default = 0,
            help = 'value of histogram bin width. (Ex. --hist-bins-width 0.7) [default: auto]'\
                    '\n[CAUTION] If combined with --hist-bins, --hist-bins takes precedence.')
    parser.add_argument("--hist-bins", type = int, default = 0,
            help = 'number of bins in hist mode. (Ex. --hist-bins 60) [default: auto]'\
                    '\n[CAUTION] If combined with --hist-bins-width, --hist-bins takes precedence.')
    parser.add_argument("--hist-cumulative", action = "store_true",
            help = 'Flag whether plot cumulative ratio with histogram')
    parser.add_argument("--hist-cumulative-color", type = str, default = "green",
            help = "Color of hitogram cumulative plot [default: green]\n(See the official matplotlib site for color choices. "\
                    "https://matplotlib.org/stable/gallery/color/named_colors.html)")
    parser.add_argument("--hist-peak-highlight", action = "store_true",
            help = "Flag whether the major peaks of the histogram are drawn as vertical lines")
    parser.add_argument("--hist-peak-highlight-color", type = str, default = "red",
            help = "Color of histogram highlight bar [default: red]\n(See the official matplotlib site for color choices. "\
                    "https://matplotlib.org/stable/gallery/color/named_colors.html) ")

    # bar mode option
    parser.add_argument("--bar-width", type = float, default = 0.8,
            help = "Value of bar width [default: 0.8]")



    return parser.parse_args()


#===========================================================================


def common_plotter(args):

    # data input
    print("[INFO] input x-data type is read as {}".format(args.xtype), file = sys.stdout)
    print("[INFO] input y-data type is read as {}".format(args.ytype), file = sys.stdout)

    if args.mode == "plot" or args.mode == "scatter":
        xdata, ydata = data_parser(args)

    elif args.mode == "hist":
        if args.ydata != "-":
            print("[WARN] If hist mode, inputed ydata is ignored", file = sys.stdout)
        if args.xdata == "-":
            xdata = data_from_pipe1(args.xtype)
        else:
            xdata = data_from_file(args.xdata, args.xtype)

        # bin num
        if args.hist_bins == 0 and args.hist_bins_width == 0:
            # Sturges' rule.
            print("[INFO] number of histogram bins is determined by Sturges's rurle", file = sys.stdout)
            bins = int(np.log2(len(xdata))) + 1
            """
            # Freedman Diaconis' choice
            print("[INFO] number of histogram bins is determined by Freedman–Diaconis' choice", file = sys.stdout)
            q75, q25 = np.percentile(data, [75 ,25])
            iqr = q75 - q25
            bins = int(2 * iqr / pow(len(data), 1/3))
            """
        else:
            if args.hist_bins_width != 0:
                bins = int(args.hist_bins_width * len(xdata))
            if args.hist_bins != 0:
                bins = args.hist_bins
            if args.hist_bins != 0 and args.hist_bins_width != 0:
                print("[WARN] When --hist-bins-width and --hist-bins are used together, --hist-bins takes precedence")
        print("[INFO] number of histogram bins : {}".format(bins), file = sys.stdout)

    elif args.mode == "bar":
        xdata, ydata = data_parser(args)
    elif args.mode == "pie":
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
    if args.seaborn_off == False:
        sns.set(style = "darkgrid", palette = "muted", color_codes = True)
    fig, ax = plt.subplots()
    ax.set_xlabel(args.xlabel)
    if args.mode == "pie" and args.xlabel == "x":
        ax.set_xlabel(" ")
    ax.set_ylabel(args.ylabel)
    if args.mode == "pie" and args.ylabel == "y":
        ax.set_ylabel(" ")
    if args.title == "t=p":
        ax.set_title(args.prefix)
    else:
        ax.set_title(args.title)
    ## hist mode only
    if args.mode == "hist":
        if args.ylabel == "y":
            ylabel = "Frequency"
        ax.set_ylabel(args.ylabel)



    # set log scale
    if args.xlog == True:
        print("[INFO] set x-axis log scale", file = sys.stdout)
        plt.xscale('log')
    if args.ylog == True:
        print("[INFO] set y-axis log scale", file = sys.stdout)
        plt.yscale('log')


    # Mode selection
    legend_list = []
    print("[INFO] Main plot color is {}".format(args.color), file = sys.stdout)

    if args.mode == "plot":
        plots = ax.plot(xdata, ydata, color = args.color, label = args.label)
        if args.label != None:
            legend_list.append(plots[0])

    elif args.mode == "scatter":
        scatters = ax.scatter(xdata, ydata, color = args.color, label = args.label)
        if args.label != None:
            legend_list.append(scatters[0])

    elif args.mode == "hist":
        n, bins, patches = ax.hist(xdata, bins = bins, color = args.color, label = args.label)
        if args.label != None:
            legend_list.append(patches[0])
        if args.hist_peak_highlight == True:
            print("[INFO] plot with hist peak highlight bar", file = sys.stdout)
            hist_peak_list = np.linspace(np.min(bins) + (bins[1] - bins[0]) / 2, np.max(bins) - (bins[1] - bins[0]) / 2, len(bins)-1)
            hist_peak = hist_peak_list[np.argmax(n)]
            lines = plt.vlines(hist_peak, 0, n[np.argmax(n)] * 1.1, color = args.hist_peak_highlight_color, label = "peak : x = {}".format(hist_peak))
            print("[INFO] Color of histogram peak highlight bar is {}".format(args.hist_peak_highlight_color), file = sys.stdout)
            legend_list.append(lines)
        if args.hist_peak_highlight == True:
            print("[INFO] plot with cumulative ratio", file = sys.stdout)
            n, bins, patches = ax.hist(xdata, alpha = 0.7, bins = bins, color = args.color, label = args.label)
            y2 = np.add.accumulate(n) / n.sum()
            x2 = np.convolve(bins, np.ones(2) / 2, mode="same")[1:]
            ax2 = ax.twinx()
            lines = ax2.plot(x2, y2, ls = "--", color = args.hist_cumulative_color, label = "culative ratio")
            print("[INFO] Color of histogram cumulative ratio plot is {}".format(args.hist_cumulative_color), file = sys.stdout)
            legend_list.append(lines[0])

    elif args.mode == "box":
        pass

    elif args.mode == "violin":
        pass

    elif args.mode == "pie":
        pie = ax.pie(ydata, labels = xdata, autopct="%.1f%%", pctdistance=0.7)

    elif args.mode == "bar":
        bar = ax.bar(xdata, ydata, color = args.color, label = args.label, width = args.bar_width)
        if args.label != None:
            legend_list.append(bar)

    elif args.mode == "empty":
        pass

    else:
        print("[ERROR] Unknown mode", file = sys.stderr)
        sys.exit(1)



    # plot additional line
    if args.xline != None:
        xlines_list = lines_parser(args.xline)
        for i in range(0, len(xlines_list)):
            xline = ax.axvline(xlines_list[i], color = args.xline_color, label = "x = {}".format(xlines_list[i]))
            print("[INFO] plot additional xline at {}".format(xlines_list[i]), file = sys.stdout)
            legend_list.append(xline)
        print("[INFO] color of addtional xline is {}".format(args.xline_color), file = sys.stdout)
    if args.yline != None:
        ylines_list = lines_parser(args.yline)
        for i in range(0, len(ylines_list)):
            yline = ax.axhline(ylines_list[i], color = args.yline_color, label = "x = {}".format(ylines_list[i]))
            print("[INFO] plot additional yline at {}".format(ylines_list[i]), file = sys.stdout)
            legend_list.append(yline)
        print("[INFO] color of addtional yline is {}".format(args.yline_color), file = sys.stdout)




    # label
    if len(legend_list) != 0:
        print("[INFO] assign labels", file = sys.stdout)
        plt.legend(handles = legend_list)
    else:
        print("[WARN] NOT assign label", file = sys.stdout)


    # grid
    if args.grid_off == True:
        print("[INFO] set grid off", file = sys.stdout)
        ax.grid()
        plt.grid()


    # data plotting range
    if args.xlim != None:
        xmin, xmax = range_parser(args.xlim)
        plt.xlim(xmin, xmax)
    if args.ylim != None:
        ymin, ymax = range_parser(args.ylim)
        plt.ylim(ymin, ymax)



    # Make margins transparent
    if args.transparent == True:
        print("[INFO] set background transparent", file = sys.stdout)
        fig.patch.set_alpha(0)



    # save figure
    fig.tight_layout()
    if args.jpg :
        print("[INFO] output picture is {}".format(args.prefix + ".jpg"), file = sys.stdout)
        plt.savefig(args.prefix + ".jpg")
    else :
        print("[INFO] output picture is {}".format(args.prefix + ".png"), file = sys.stdout)
        plt.savefig(args.prefix + ".png")



#===========================================================================


def lines_parser(lines):

    print("[INFO] plotting lines parser is called", file = sys.stdout)

    if "[" not in lines:
        print("[ERROR] plotting lines parser error, not include \"[\"", file = sys.stderr)
        print("[ERROR] For --xline or --yline, use \"[-1.2]\" or \"[10,100, ...]\" as example", file = sys.stderr)
        sys.exit(1)


    if "]" not in lines:
        print("[ERROR] plotting lines parser error, not include \"]\"", file = sys.stderr)
        print("[ERROR] For --xline or --yline, use \"[-1.2]\" or \"[10,100, ...]\" as example", file = sys.stderr)
        sys.exit(1)


    lines = lines.lstrip("[").rstrip("]")

    try:
        lines_list = lines.split(",")
        lines_list = list(map(float, lines_list))

    except:
        lines_list = [float(lines)]


    return lines_list




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

    print("[INFO] set plotting range [{}:{}]".format(min_,max_), file = sys.stdout)

    return min_, max_


#===========================================================================


def data_from_pipe2(args):

    print("[INFO] 2 pipe input execute", file = sys.stdout)
    xdata = []
    ydata = []

    for line in sys.stdin:

        if args.split == "\\t":
            a = line.split("\t")
        else:
            a = line.split(args.split)


        if args.xtype == "float":
            xdata.append(float(a[0]))

        if args.xtype == "int":
            xdata.append(int(a[0]))

        if args.xtype == "str":
            xdata.append(str(a[0]))

        if args.ytype == "float":
            ydata.append(float(a[1]))

        if args.ytype == "int":
            ydata.append(int(a[1]))

        if args.ytype == "str":
            ydata.append(str(a[1]))

    return xdata, ydata


def data_from_pipe1(data_type):

    print("[INFO] 1 pipe input execute", file = sys.stdout)

    data = []

    for line in sys.stdin:


        if data_type == "float":
            data.append(float(line.split("\n")[0]))

        if data_type == "int":
            data.append(int(line.split("\n")[0]))

        if data_type == "str":
            data.append(str(line.split("\n")[0]))

    return data


def data_from_file(file, data_type):

    print("[INFO] file input execute", file = sys.stdout)

    data = []

    with open(file) as ref:

        for line in ref:

            if data_type == "float":
                data.append(float(line.split("\n")[0]))

            if data_type == "int":
                data.append(int(line.split("\n")[0]))

            if data_type == "str":
                data.append(str(line.split("\n")[0]))

    return data



def data_parser(args):

    if args.xdata == "-" and args.ydata == "-":
        return data_from_pipe2(args)

    elif args.xdata == "-" and args.ydata != "-":
        return data_from_pipe1(args.xtype), data_from_file(args.ydata, args.ytype)

    elif args.xdata == "-" and args.ydata != "-":
        return data_from_file(args.xdata, args.xtype), data_from_pipe1(args.ytype)

    else:
        return data_from_file(args.xdata, args.xtype), data_from_file(args.ydata, args.ytype)


#===========================================================================


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


#===========================================================================


# main
if __name__ == "__main__":

    # arg
    args = arg_parser()

    # mode
    print("[INFO] {} mode".format(args.mode), file = sys.stdout)

    common_plotter(args)

    print("[INFO] tmplot.py done", file = sys.stdout)

