from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Plot(CommonPlotter):
    def run(self) -> None:
        self.ax.plot(
            self.xdata, self.ydata, color=self.args.color, label=self.args.label
        )
        self.save()
