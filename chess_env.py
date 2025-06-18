# chess.py
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

class ChessEnv:
    def __init__(self):
        self.board = self._init_board()
        self.done = False

    def _init_board(self):
        board = [["" for _ in range(8)] for _ in range(8)]
        for i in range(8):
            board[1][i] = "P"  # Dummy pawns
        return board

    def reset(self):
        self.board = self._init_board()
        self.done = False
        return self.board

    def step(self, action):
        if self.done:
            return self.board, 0, self.done

        # Dummy logic: move pawn from action[0] to action[1]
        start, end = action
        x1, y1 = start
        x2, y2 = end

        if self.board[x1][y1] == "P" and self.board[x2][y2] == "":
            self.board[x2][y2] = "P"
            self.board[x1][y1] = ""
            reward = 1
        else:
            reward = -1

        self.done = random.random() < 0.1  # 10% chance to end
        return self.board, reward, self.done

    def render(self):
        for row in self.board:
            print(" ".join(piece or "." for piece in row))

# Singleton environment
env = ChessEnv()

@app.route("/reset", methods=["POST"])
def reset():
    board = env.reset()
    return jsonify({"board": board})

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action", [])
    board, reward, done = env.step(action)
    return jsonify({"board": board, "reward": reward, "done": done})

if __name__ == "__main__":
    app.run(port=5000)
