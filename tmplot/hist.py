from dataclasses import dataclass

import seaborn as sns
from matplotlib import pyplot as plt

from .common import CommonPlotter


@dataclass
class Hist(CommonPlotter):
    def run(self) -> None:
        # seaborn
        if self.args.seaborn_off is False:
            sns.set(style="darkgrid", palette="muted", color_codes=True)

        # grid
        if self.args.grid_off is False:
            plt.grid(True)

        # figure prepare
        fig, ax = plt.subplots(figsize=(self.fig_width, self.fig_height))
        ax.set_xlabel(self.args.xlabel)
        ax.set_ylabel(self.args.ylabel)
        ax.set_title(self.args.title)

        # hist
        ax.hist(self.xdata, color=self.args.color)

        # plot range
        if self.args.xlim is not None:
            plt.xlim(xmin, xmax)

        if self.args.ylim is not None:
            plt.ylim(ymin, ymax)

        # save
        fig.tight_layout()
        if self.args.out is not None:
            plt.savefig(self.args.out)
        else:
            plt.show()
