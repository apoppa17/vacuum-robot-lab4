"""Tabular Q-learning agent (knows nothing about the grid layout).

Update rule:
    Q(s, a) <- Q(s, a) + alpha * (r + gamma * max_a' Q(s', a') - Q(s, a))

Hyperparameters:
    alpha   (learning rate): how far each update moves toward the new target.
            High = fast but noisy; low = stable but slow.
    gamma   (discount):      how much future reward matters.
            Near 1 = far-sighted; near 0 = greedy for immediate reward.
    epsilon (exploration):   probability of a random action (epsilon-greedy).
            High = more exploration; low = more exploitation.
    The living reward is an environment setting (see environment.py).
"""

import random


class QLearningAgent:
    """Tabular epsilon-greedy Q-learning agent."""

    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1, seed=None):
        self.actions = list(actions)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_values = {}  # (state, action) -> value, defaults to 0.0
        self.rng = random.Random(seed)

    def get_q(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def best_value(self, state):
        return max(self.get_q(state, action) for action in self.actions)

    def best_action(self, state):
        """Greedy action, breaking ties randomly."""
        best = self.best_value(state)
        tied = [a for a in self.actions if self.get_q(state, a) == best]
        return self.rng.choice(tied)

    def choose_action(self, state):
        """Epsilon-greedy policy."""
        if self.rng.random() < self.epsilon:
            return self.rng.choice(self.actions)
        return self.best_action(state)

    def update(self, state, action, reward, next_state, done):
        """Apply one Q-learning update for the observed transition."""
        # A terminal next state has no future value.
        future_value = 0.0 if done else self.best_value(next_state)
        target = reward + self.gamma * future_value
        old = self.get_q(state, action)
        self.q_values[(state, action)] = old + self.alpha * (target - old)


def train(env, agent, episodes=1000, max_steps=100):
    """Run Q-learning; returns total reward per episode.

    An episode also ends after max_steps. In that case `done` is False, so the
    update still bootstraps from the next state's value (a time-limit cut-off
    is not a true terminal state).
    """
    returns = []
    for _ in range(episodes):
        state = env.reset()
        total = 0.0
        for _ in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state
            total += reward
            if done:
                break
        returns.append(total)
    return returns
