"""Grid environment for the vacuum robot (no learning logic lives here).

Provided requirements (from CLAUDE.md):
    - 4x4 grid, coordinates are (row, column) starting at 0.
    - Start at (0, 0), obstacle at (1, 1).
    - Reward -1 at (3, 1), reward +10 at goal (3, 3), 0 everywhere else.

ASSUMPTIONS (the transition model T and full reward function R are NOT provided):
    - Movement is deterministic (no slip probabilities are assumed).
    - Moving off the grid or into the obstacle leaves the robot in place.
    - The reward is received for the cell the robot ends up in. A bump into a
      wall or the obstacle leaves the robot in place, so it pays that same
      cell's reward again (e.g. bumping while on (3, 1) returns -1 each time).
    - Reaching the goal (3, 3) ends the episode. The (3, 1) cell is not terminal.
    - `living_reward` is added on every step; it defaults to 0 because the
      spec says all other cells have a value of 0.
"""

GRID_SIZE = 4
START_STATE = (0, 0)
OBSTACLE = (1, 1)
GOAL_STATE = (3, 3)
CELL_REWARDS = {(3, 1): -1.0, GOAL_STATE: 10.0}

# Action name -> (row delta, column delta)
ACTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


class VacuumEnvironment:
    """4x4 vacuum grid with a deterministic (assumed) transition model."""

    def __init__(self, living_reward=0.0):
        self.living_reward = living_reward
        self.state = START_STATE

    @property
    def actions(self):
        """Names of the available actions."""
        return list(ACTIONS)

    @property
    def states(self):
        """All reachable (row, col) cells; the obstacle is excluded."""
        return [
            (row, col)
            for row in range(GRID_SIZE)
            for col in range(GRID_SIZE)
            if (row, col) != OBSTACLE
        ]

    def reset(self):
        """Put the robot back at the start and return the start state."""
        self.state = START_STATE
        return self.state

    def is_terminal(self, state):
        """True if the state is the goal, which ends the episode."""
        return state == GOAL_STATE

    def step(self, action):
        """Apply an action. Returns (next_state, reward, done).

        Raises ValueError for an unknown action, and RuntimeError if the
        episode already ended (call reset() first).
        """
        if action not in ACTIONS:
            raise ValueError(f"Unknown action {action!r}; expected one of {list(ACTIONS)}")
        if self.is_terminal(self.state):
            raise RuntimeError("Episode is over; call reset() before step().")
        d_row, d_col = ACTIONS[action]
        row, col = self.state[0] + d_row, self.state[1] + d_col
        candidate = (row, col)

        in_bounds = 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE
        if in_bounds and candidate != OBSTACLE:
            self.state = candidate

        reward = self.living_reward + CELL_REWARDS.get(self.state, 0.0)
        return self.state, reward, self.is_terminal(self.state)
