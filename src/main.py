import matplotlib.pyplot as plt
import test_instances as ti
import numpy as np
from pathlib import Path  # Pour manipuler les chemins de fichiers
from glob import glob  # Pour rechercher des fichiers
import random
import utils as ut
from scipy.spatial.distance import pdist, squareform
import clarke_and_wright as cw
import os
import csv


def exec(path):
    n,m,tmax,coords = ut.read_problem_instance(path)
    start = coords.iloc[0]
    end = coords.iloc[-1]

    # Compute pairwise Euclidean distances
    distances = pdist(coords[['x', 'y']], metric='euclidean')

    # Compute time matrix
    v = 1
    time = distances / v

    # Create a square time matrix
    time_matrix = squareform(time)

    
    # Compute VRP initial savings
    savings = ut.vrp_savings(time_matrix, n)

    # Compute Clarke and Wright Savings
    alpha = ut.alpha(coords)

    init_solution, banned_routes = ut.init_solution(time_matrix, coords, n, tmax)
    sorted_top_savings_list = ut.top_savings(coords, savings, alpha, n, banned_routes)

    solution = cw.clarke_wright(init_solution, sorted_top_savings_list, tmax, time_matrix, n, m)
    profit = solution['profit'].sum()
    
    return profit


def process_files(input_folder, output_csv):
    # Get a list of all files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Process each file and collect results
    results = []
    for file_name in files:
        file_path = os.path.join(input_folder, file_name)

        # Process the file (replace this with your actual processing logic)
        result = exec(file_path)

        # Append the result to the list
        results.append({'File': file_name, 'Result': result})

    # Write the results to a CSV file
    write_to_csv(results, output_csv)


def write_to_csv(results, output_csv):
    # Write the results to a CSV file in append mode
    with open(output_csv, 'a', newline='') as csv_file:  # Use 'a' for append mode
        fieldnames = ['File', 'Result']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the file is empty, if so, write the header
        if csv_file.tell() == 0:
            writer.writeheader()

        # Write the data
        for row in results:
            writer.writerow(row)

if __name__ == "__main__":
# Specify the input folder and output CSV file
    instances_path = ["TestInstances/Chao/Set_64_234", "TestInstances/Chao/Set_66_234", "TestInstances/Chao/Set_100_234", "TestInstances/Chao/Set_102_234", "TestInstances/Tsiligirides/Set_21_234", "TestInstances/Tsiligirides/Set_32_234", "TestInstances/Tsiligirides/Set_33_234"]
    output_csv_path = "output_results_or-opt.csv"  # Replace with your desired output CSV file path

    # Process files and write results to CSV
    for path in instances_path:
        process_files(path, output_csv_path)