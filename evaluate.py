import torch
from agent import ChessAgent
from chess_env import ChessEnv
from config import MODEL_SAVE_PATH

env = ChessEnv()
agent = ChessAgent(state_dim=773, action_dim=4672)
agent.model.load_state_dict(torch.load(MODEL_SAVE_PATH))
agent.model.eval()

# Evaluation loop here
