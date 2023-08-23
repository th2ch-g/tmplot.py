from dataclasses import dataclass
import argparse
from matplotlib import pyplot as plt
import sys
from .logger import generate_logger

LOGGER = generate_logger(__name__)

@dataclass
class Asm():
    args: argparse.ArgumentParser
    def run(self) -> None:
        # cat file read
        if self.args.file == "-":
            input_source = sys.stdin
        else:
            input_source = open(self.args.file)
        for idx, line in enumerate(input_source):
            line = line.rstrip()
            if idx == 0:
                # prepare figure
                pass

            # plot by each mode

        # save
        fig.tight_layout()
        if self.args.out is not None:
            plt.savefig(self.args.out)
            LOGGER.info(f"figure name is {self.args.out}")
        else:
            LOGGER.info("No file output. Will use additional window")
            plt.show()
