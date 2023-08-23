from dataclasses import dataclass

from .common import CommonPlotter

@dataclass
class Cat(CommonPlotter):
    def run(self) -> None:
        # file output or stdout
        if self.args.out is not None:
            with open(self.args.out, mode="a") as ref:
                ref.write(f"{self}\n")
        else:
            print(self)
