from dataclasses import dataclass
from .common import CommonPlotter

@dataclass
class Plot(CommonPlotter):
    def run(self) -> None:
        for data in self.data:
            self.ax1.plot(data[:, 0], data[:, 1])
        self.save()
