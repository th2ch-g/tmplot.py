from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Scatter(CommonPlotter):
    def run(self) -> None:
        self.ax.scatter(self.xdata, self.ydata, color=self.args.color)
        self.save()
