import os
from glob import glob
from dataclasses import dataclass
from typing import List
import matplotlib.pyplot as plt
import pandas as pd

@dataclass
class TestInstance:
    name: str
    n: int  # number of clients + 2 (depot and end)
    m: int  # number of vehicules
    tmax: float  # available time budget per path
    x_coordinates: List[float]  # x coordinates
    y_coordinates: List[float]  # y coordinates
    scores: List[int]  # scores
    
    def __repr__(self) -> str:
        return f"TestInstance(name='{self.name}', n={self.n}, m={self.m}, tmax={self.tmax}, " \
               f"x_coordinates={self.x_coordinates}, y_coordinates={self.y_coordinates}, scores={self.scores})"

    def plot_instance(self):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.x_coordinates, self.y_coordinates, s=50)
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
            
            # Separate data into x, y, and score lists
            x_coordinates = [x for x, _, _ in data]
            y_coordinates = [y for _, y, _ in data]
            scores = [score for _, _, score in data]
            
        if test_set not in test_dict:
            test_dict[test_set] = []
        instance = TestInstance(name=name, n=n, m=m, tmax=tmax,
                                x_coordinates=x_coordinates, y_coordinates=y_coordinates, scores=scores)
        test_dict[test_set].append(instance)
        # Plot each instance after creation
        # instance.plot_instance()
    return test_dict


def plot_instance_points(instance: TestInstance):
    plt.figure(figsize=(8, 6))
    plt.scatter(instance.x_coordinates, instance.y_coordinates, s=50)
    plt.title(f"Instance: {instance.name}")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.show()