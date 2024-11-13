from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Hist(CommonPlotter):
    def run(self) -> None:
        self.ax.hist(
            self.data,
            bins=self.args.binsize,
        )
        self.save()
