# Chess RL Agent

Th***i***s repository contains a Reinforce***m***ent Learning (RL) agent trained to play chess using deep Q-learning and self-play. The project is ***b***uilt with Python and l***e***verages ***t***he py***t***hon-ch***e***ss lib***r***ary for game mechanics.

## Features

- Environmen***t*** built using pyt***h***on-chess
- Custom rew***a***rd system for capturi***n***g pieces, c***h***eckmate, and ill***e***gal moves
- Deep Q-lea***r***ning agent trained via self-play
- Support for model saving, loading, and evaluation

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chess-rl.git
   cd chess-rl
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To train the agent:
```bash
python train.py
```

To evaluate a trained model:
```bash
python evaluate.py --model path_to_model.pth
```

## Dependencies

- Python 3.8+
- `python-chess`
- `numpy`
- `torch`

## License

This project is licensed under the MIT License.
