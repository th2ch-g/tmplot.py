from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Hist(CommonPlotter):
    def run(self) -> None:
        self.ax.hist(self.xdata, color=self.args.color, label=self.args.label)
        self.save()
