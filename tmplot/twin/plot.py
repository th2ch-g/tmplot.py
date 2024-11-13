from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Plot(CommonPlotter):
    def run(self) -> None:
        self.ax2.plot(self.data[:, 0], self.data[:, 1])
        self.ax2.plot(self.data[:, 0], self.data[:, 2])
        self.save()
