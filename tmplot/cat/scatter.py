
from dataclasses import dataclass
from .common import CommonPlotter

@dataclass
class Scatter(CommonPlotter):
    def run(self) -> None:
        for data in self.data:
            self.ax1.scatter(data[:, 0], data[:, 1])
        self.save()
