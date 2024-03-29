import sys
from dataclasses import dataclass

from .common import CommonPlotter


@dataclass
class Cat(CommonPlotter):
    def run(self) -> None:
        # file output or stdout
        if self.args.out is not None:
            with open(self.args.out, mode="a") as ref:
                ref.write(f"{self.output()}\n")
        else:
            print(self.output())

    def output(self) -> str:
        try:
            out = f"""# tmplot-cat-mode-start
mode={sys.argv[2]}
xtype={self.args.xtype}
ytype={self.args.ytype}
color={self.args.color}
title={self.args.title}
label={self.args.label}
grid_off={self.args.grid_off}
xlabel={self.args.xlabel}
ylabel={self.args.ylabel}
xmin={self.xmin}
xmax={self.xmax}
ymin={self.ymin}
ymax={self.ymax}
fig_width={self.fig_width}
fig_height={self.fig_height}
xdata={self.xdata}
ydata={self.ydata}
bins={self.args.bins}
# tmplot-cat-mode-end"""
        except Exception:
            out = f"""# tmplot-cat-mode-start
mode={sys.argv[2]}
xtype={self.args.xtype}
ytype={self.args.ytype}
color={self.args.color}
title={self.args.title}
label={self.args.label}
grid_off={self.args.grid_off}
xlabel={self.args.xlabel}
ylabel={self.args.ylabel}
xmin={self.xmin}
xmax={self.xmax}
ymin={self.ymin}
ymax={self.ymax}
fig_width={self.fig_width}
fig_height={self.fig_height}
xdata={self.xdata}
ydata={self.ydata}
# tmplot-cat-mode-end"""
        return out
