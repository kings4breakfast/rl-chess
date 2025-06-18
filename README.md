# Chess bot using Reinforcement Learning

This repository contains a Reinforcement Learning (RL) agent trained to play chess using deep Q-learning and self-play. The project is built with Python and leverages the python-chess library for game mechanics.

## Features

* Environment built using python-chess
* Custom reward system for capturing pieces, checkmate, and illegal moves
* Deep Q-learning agent trained via self-play
* Support for model saving, loading, and evaluation

## Setup

1. Clone the repository:

   bash
   git clone https://github.com/kings4breakfast/rl-chess.git
   cd chess-rl
   

2. Install dependencies:

   bash
   pip install -r requirements.txt
   

## Usage

To train the agent:

bash
python train.py


To evaluate a trained model:

bash
python evaluate.py --model path_to_model.pth


## Dependencies

* Python 3.8+
* python-chess
* numpy
* torch

## License

This project is licensed under the MIT License.
