from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Scatter(CommonPlotter):
    def run(self) -> None:
        self.ax2.scatter(self.data[:, 0], self.data[:, 1])
        self.ax2.scatter(self.data[:, 0], self.data[:, 2])
        self.save()
