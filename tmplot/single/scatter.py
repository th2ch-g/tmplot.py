from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Scatter(CommonPlotter):
    def run(self) -> None:
        self.ax.scatter(self.data[:, 0], self.data[:, 1])
        self.save()
