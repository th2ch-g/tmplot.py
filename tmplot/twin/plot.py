from dataclasses import dataclass
from .common import CommonPlotter


@dataclass
class Plot(CommonPlotter):
    def run(self) -> None:
        self.ax2.plot(
            self.xdata, self.ydata,
        )
        self.save()
