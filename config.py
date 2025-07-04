# Configuration for training
NUM_EPISODES = 10000
LEARNING_RATE = 1e-4
GAMMA = 0.99
EPSILON_START = 1.0
EPSILON_END = 0.1
EPSILON_DECAY = 0.995
REPLAY_MEMORY_SIZE = 10000
BATCH_SIZE = 64
TARGET_UPDATE_FREQ = 10
MODEL_SAVE_PATH = "saved_models/dqn_chess.pth"
