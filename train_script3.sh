#!/bin/sh
nohup python -u /home/irelia/self_play_with_reward_and_train.py --max_simulation=500 --save_dir=/home/irelia/checkpoint7 --print_mcts_search=False --print_mcts_tree=False --c_puct=0.5 --reward_ratio=2 --epoch=30 > l7 &
nohup python -u /home/irelia/self_play_with_reward_and_train.py --max_simulation=500 --save_dir=/home/irelia/checkpoint8 --print_mcts_search=False --print_mcts_tree=False --c_puct=1 --reward_ratio=2 --epoch=30 > l8 &
nohup python -u /home/irelia/self_play_with_reward_and_train.py --max_simulation=500 --save_dir=/home/irelia/checkpoint9 --print_mcts_search=False --print_mcts_tree=False --c_puct=2 --reward_ratio=2 --epoch=30 > l9 &