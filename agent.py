import torch
import random
import numpy as np
from collections import deque
from model import DQN
from config import *

class ChessAgent:
    def __init__(self, state_dim, action_dim):
        self.model = DQN(state_dim, action_dim)
        self.target_model = DQN(state_dim, action_dim)
        self.memory = deque(maxlen=REPLAY_MEMORY_SIZE)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=LEARNING_RATE)
        self.epsilon = EPSILON_START
        self.action_dim = action_dim

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_dim - 1)
        with torch.no_grad():
            return torch.argmax(self.model(state)).item()

    def store_transition(self, transition):
        self.memory.append(transition)

    def train_step(self):
        if len(self.memory) < BATCH_SIZE:
            return
        # Training logic here
