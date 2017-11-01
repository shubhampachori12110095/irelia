from game.game import Game
import traceback
from game import korean_chess_constant as c
import random

init_state = [[[0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9],
              [[0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9],
              [[1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9]]
init_state[1][1][3] = c.KING
init_state[0][8][5] = c.KING
init_state[0][6][4] = c.CAR
init_state[0][5][4] = c.CAR
# env = Game.make("KoreanChess-v1", {"init_state": init_state})
env = Game.make("KoreanChess-v1")

env.reset()

for i in range(100):
    if i % 2 == 1:
        while True:
            from_x = raw_input("from X number : ")
            if from_x.isdigit():
                from_x = int(from_x)
                break
        while True:
            from_y = raw_input("from Y number : ")
            if from_y.isdigit():
                from_y = int(from_y)
                break
        while True:
            to_x = raw_input("to X number : ")
            if to_x.isdigit():
                to_x = int(to_x)
                break
        while True:
            to_y = raw_input("to Y number : ")
            if to_y.isdigit():
                to_y = int(to_y)
                break

        try:
            new_state, reward, done, _ = env.step({"from_x": from_x, "from_y": from_y, "to_x": to_x, "to_y": to_y})

            if done:
                print("The End")
                break

        except Exception as e:
            print(e.message)
            traceback.print_exc()
    else:
        actions = env.get_actions()
        action = actions[random.randint(0, len(actions) - 1)]
        new_state, reward, done, _ = env.step(
            {"from_x": action["from_x"], "from_y": action["from_y"], "to_x": action["to_x"],
             "to_y": action["to_y"]})

        if done:
            print("The End")
            break
