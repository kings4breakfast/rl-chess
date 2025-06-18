from chess_env import ChessEnv
from agent import ChessAgent
from config import *

env = ChessEnv()
agent = ChessAgent(state_dim=773, action_dim=4672)  # Example dimensions

for episode in range(NUM_EPISODES):
    state = env.reset()
    done = False
    while not done:
        action = agent.select_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.store_transition((state, action, reward, next_state, done))
        agent.train_step()
        state = next_state
