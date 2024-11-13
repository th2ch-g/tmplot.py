
from dataclasses import dataclass
from .common import CommonPlotter

@dataclass
class Hist(CommonPlotter):
    def run(self) -> None:
        for data in self.data:
            self.ax1.hist(data[:, 0])
        self.save()
