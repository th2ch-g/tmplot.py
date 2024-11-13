from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Scatter(CommonPlotter):
    def run(self) -> None:
        self.ax2.scatter(
            self.xdata,
            self.ydata,
        )
        self.save()
