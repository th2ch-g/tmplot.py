import argparse
import sys
from dataclasses import dataclass
from typing import Any, List

from matplotlib import pyplot as plt

from .logger import generate_logger

LOGGER = generate_logger(__name__)


@dataclass
class Asm:
    args: argparse.ArgumentParser

    def run(self) -> None:
        # cat file read
        if self.args.file == "-":
            input_source = sys.stdin
        else:
            input_source = open(self.args.file)
        cat_num = 0
        cat_start = False
        for line in input_source:
            line = line.rstrip()
            # parse
            if "# tmplot-cat-mode-start" in line:
                cat_start = True
            elif "# tmplot-cat-mode-end" in line:
                cat_start = False
                cat_num += 1
            elif "mode=" in line:
                mode = line.split("mode=")[1]
            elif "xtype=" in line:
                xtype = line.split("xtype=")[1]
            elif "ytype=" in line:
                ytype = line.split("ytype=")[1]
            elif "color=" in line:
                color = line.split("color=")[1]
                if color == "None":
                    color = None
            elif "title=" in line:
                title = line.split("title=")[1]
            elif "grid_off=" in line:
                grid_off = line.split("grid_off=")[1]
                if grid_off == "False":
                    grid_off = False
                else:
                    grid_off = True
            elif "xlabel=" in line:
                xlabel = line.split("xlabel=")[1]
            elif "ylabel=" in line:
                ylabel = line.split("ylabel=")[1]
            elif "label=" in line:
                label = line.split("label=")[1]
                if label == "None":
                    label = None
            elif "xmin=" in line:
                xmin = line.split("xmin=")[1]
                if xmin != "None":
                    print(xmin)
                    xmin = float(xmin)
            elif "xmax=" in line:
                xmax = line.split("xmax=")[1]
                if xmax != "None":
                    xmax = float(xmax)
            elif "ymin=" in line:
                ymin = line.split("ymin=")[1]
                if ymin != "None":
                    ymin = float(ymin)
            elif "ymax=" in line:
                ymax = line.split("ymax=")[1]
                if ymax != "None":
                    ymax = float(ymax)
            elif "fig_width=" in line:
                fig_width = line.split("fig_width=")[1]
                fig_width = float(fig_width)
            elif "fig_height=" in line:
                fig_height = line.split("fig_height=")[1]
                fig_height = float(fig_height)
            elif "xdata=" in line:
                xdata = line.split("xdata=")[1]
                xdata = self.line_data_parse(xdata, xtype)
            elif "ydata=" in line:
                ydata = line.split("ydata=")[1]
                ydata = self.line_data_parse(ydata, ytype)

            if cat_num == 1 and cat_start is False:
                # prepare figure
                fig, ax = plt.subplots(figsize=(fig_width, fig_height))
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.set_title(title)
                if grid_off is False:
                    ax.grid()
                    LOGGER.info("grid on")
                if xmin != "None" and xmax != "None":
                    LOGGER.info(f"xlim: {xmin}:{xmax}")
                    plt.xlim(xmin, xmax)
                if ymin != "None" and ymax != "None":
                    LOGGER.info(f"ylim: {ymin}:{ymax}")
                    plt.ylim(ymin, ymax)
                LOGGER.info("figure was prepared")
            if cat_start is False:
                # plot by each mode
                if mode == "plot":
                    LOGGER.info("plot mode called")
                    ax.plot(xdata, ydata, color=color, label=label)
                elif mode == "scatter":
                    LOGGER.info("scatter mode called")
                    ax.scatter(xdata, ydata, color=color, label=label)
                elif mode == "hist":
                    LOGGER.info("hist mode called")
                    ax.hist(xdata, ydata, color=color, label=label)
                if label is not None:
                    plt.legend()
        # save
        fig.tight_layout()
        if self.args.out is not None:
            plt.savefig(self.args.out)
            LOGGER.info(f"figure name is {self.args.out}")
        else:
            LOGGER.info("No file output. Will use additional window")
            plt.show()

    def line_data_parse(self, data: str, data_type: str) -> List[Any]:
        data = data.replace("[", "")
        data = data.replace("]", "")
        data = data.replace(", ", ",")
        data_list = data.split(",")
        out_list = []
        for d in data_list:
            if data_type == "float":
                out_list.append(float(d))
            elif data_type == "int":
                out_list.append(int(d))
            elif data_type == "str":
                out_list.append(str(d))
        return out_list
