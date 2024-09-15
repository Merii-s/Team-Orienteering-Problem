# Team Orienteering Problem (TOP) Project

## Overview

The Team Orienteering Problem (TOP) is a combinatorial optimization problem that involves planning routes for a team of agents to maximize the total score collected from various locations while adhering to constraints such as time limits. The problem is characterized by its need to balance the selection of locations with the associated travel costs, making it relevant in fields such as logistics, transportation, and urban planning.

![TOP Diagram](data:image/png;base64,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)  

## Implementation

In this project, we developed a Python implementation of the Clark and Wright algorithm, enhanced with 2-opt and or-opt optimizations to improve the efficiency of the routing solutions. 

### Key Features

- **Clark and Wright Algorithm**: Utilizes a savings-based approach to generate initial routes for agents.
- **2-opt and Or-opt Optimizations**: These techniques refine the initial routes by reducing travel distances and improving overall efficiency.
- **Test Instances**: Problem instances used for testing the implementation are contained in the `TestInstances` folder.
- **Results**: The results for each instance are generated by the code in CSV format for easy analysis.

## Installation

To set up the project, clone the repository and install any necessary dependencies:

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

## Usage

After setting up the environment, run the main script to execute the algorithm and generate results:

```bash
python main.py
```

