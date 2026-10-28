
# Vacuum Robot Reinforcement Learning

## Project Overview
This CS440 project focuses on a vacuum robot navigating a 4x4 grid environment using reinforcement learning. The goal is to eventually implement Q-learning.

The current lab focuses on setting up context engineering strategies 1 and 4 rather than implementing the algorithm.

## Environment

| Start | 0  | 0 | 0  |
|-------|----|---|----|
| 0     | X  | 0 | 0  |
| 0     | 0  | 0 | 0  |
| 0     | -1 | 0 | 10 |

- The robot starts at (0, 0).
- X represents an obstacle at (1, 1).
- The cell at (3, 1) has a reward of -1.
- The goal at (3, 3) has a reward of +10.
- All other cells have a value of 0.
- Coordinates use (row, column), starting at 0.

The transition model (T) and complete reward function (R) are not provided.

## Development Guidelines
- Use Python for future implementation.
- Keep code readable and organized.
- Use descriptive variable and function names.
- Follow the provided environment without modifying its layout.
- Do not assume unspecified transition probabilities or environment behavior.
- Keep environment logic separate from learning algorithms.
- Do not implement Q-learning during the current lab.
- Explain important implementation decisions.
