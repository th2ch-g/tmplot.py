from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Plot(CommonPlotter):
    def run(self) -> None:
        self.ax.plot(self.data[:, 0], self.data[:, 1])
        self.save()
