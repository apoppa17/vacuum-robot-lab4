"""Train a Q-learning vacuum robot and print the learned policy."""

from environment import GRID_SIZE, OBSTACLE, VacuumEnvironment
from q_learning import QLearningAgent, train

ARROWS = {"up": "^", "down": "v", "left": "<", "right": ">"}


def print_policy(env, agent):
    """Print the greedy policy as arrows; '?' marks cells with no learned preference."""
    for row in range(GRID_SIZE):
        cells = []
        for col in range(GRID_SIZE):
            state = (row, col)
            if state == OBSTACLE:
                cells.append("X")
            elif env.is_terminal(state):
                cells.append("G")
            else:
                q_values = {agent.get_q(state, action) for action in env.actions}
                if len(q_values) == 1:  # all tied (e.g. never visited): no real preference
                    cells.append("?")
                else:
                    cells.append(ARROWS[agent.best_action(state)])
        print(" ".join(cells))


def main():
    """Train the agent on the vacuum environment and show the result."""
    env = VacuumEnvironment(living_reward=0.0)
    agent = QLearningAgent(env.actions, alpha=0.1, gamma=0.9, epsilon=0.2, seed=0)
    returns = train(env, agent, episodes=2000)

    recent_returns = returns[-100:]
    average_return = sum(recent_returns) / len(recent_returns)
    print(f"Average return, last {len(recent_returns)} episodes: {average_return:.2f}")
    print("Greedy policy (G = goal, X = obstacle):")
    print_policy(env, agent)


if __name__ == "__main__":
    main()
