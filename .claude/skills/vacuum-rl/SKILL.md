---
name: vacuum-rl
description: Reusable intructions on evaluating reinforcement learning (RL) for the vacuum robot. Explains the grid, reward system, defines Q-learning, hyperparameters, and assumptions.
---
# Vacuum Robot Reinforcement Learning Skill

## Project Environment

The project uses a 4x4 grid.

- Start position: (0, 0)
- Obstacle: (1, 1)
- Negative reward: -1 at (3, 1)
- Goal: +10 at (3, 3)
- All other cells: 0

Coordinates use (row, column), starting at zero.

## Reinforcement Learning Concepts

When discussing Q-learning, explain:

- State: The robot's current grid position.
- Action: A movement the robot can take.
- Reward: Feedback received from the environment.
- Policy: The strategy used to select actions.
- Q-value: The estimated long-term value of an action.

## Hyperparameters

Evaluate these four parameters:

- Living reward
- Discount factor (gamma)
- Learning rate (alpha)
- Exploration rate (epsilon)

Explain the purpose and tradeoffs of each.

## Development Rules

- Do not change the specified grid layout.
- Do not assume unspecified transition probabilities.
- Clearly distinguish assumptions from provided requirements.
- Keep environment logic separate from learning algorithms.
- Write readable, organized Python.
- Explain important implementation decisions.