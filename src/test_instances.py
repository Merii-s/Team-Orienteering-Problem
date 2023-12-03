from typing import List, Tuple
from dataclasses import dataclass
from glob import glob
import os
import matplotlib.pyplot as plt

@dataclass
class TestInstance:
    name: str
    n: int  # number of vertices
    m: int  # number of vehicules
    tmax: float  # available time budget per path
    data: List[Tuple[float, float, int]]  # list of (x, y, score) tuples

    def __repr__(self) -> str:
        return f"TestInstance(name='{self.name}', n={self.n}, m={self.m}, tmax={self.tmax}, data={self.data})"

    def plot_instance(self):
        x_values = [x for x, _, _ in self.data]
        y_values = [y for _, y, _ in self.data]
        plt.figure(figsize=(8, 6))
        plt.scatter(x_values, y_values, s=50)
        plt.title(f"Instance: {self.name}")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)
        plt.show()


def read_test_sets(dirpath: str):
    test_sets = glob(os.path.join(dirpath, "Set*"))
    test_dict = {}
    for filename in glob(os.path.join(dirpath, "Set*", "*.txt")):
        test_set = os.path.basename(os.path.dirname(filename))
        with open(filename) as f:
            name = os.path.splitext(os.path.basename(filename))[0]
            n = int(f.readline().split(" ")[-1])
            m = int(f.readline().split(" ")[-1])
            tmax = float(f.readline().split(" ")[-1])
            data = [tuple(map(float, line.strip().split())) for line in f.readlines()]
        if test_set not in test_dict:
            test_dict[test_set] = []
        instance = TestInstance(name=name, n=n, m=m, tmax=tmax, data=data)
        test_dict[test_set].append(instance)
        # Plot each instance after creation
        # instance.plot_instance()
    return test_dict

