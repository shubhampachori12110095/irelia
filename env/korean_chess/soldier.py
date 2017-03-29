# coding=utf8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from env.korean_chess import common


def get_actions(state_map, x, y):
    piece = state_map[y][x]
    side = piece[0]

    action_list = []

    piece_type = common.SOLDIER

    # 대각선 오른쪽 길 체크
    if ((y == 1 and x == 4) or (y == 2 and x == 3)) and \
            not common.is_our_side(state_map, x + 1, y - 1, side):
        # and not util.is_losing_way(state_map, x, y, x + 1, y - 1, side):
        action_list.append(
            {'x': x, 'y': y, 'to_x': x + 1, 'to_y': y - 1, 'direction': common.DIAGONAL_FORWARD_RIGHT1, 'step': 1,
             'piece_type': piece_type})

    # 대각선 왼쪽 길 체크
    if ((y == 1 and x == 4) or (y == 2 and x == 5)) and \
            not common.is_our_side(state_map, x - 1, y - 1, side):
        # and not util.is_losing_way(state_map, x, y, x - 1, y - 1, side):
        action_list.append(
            {'x': x, 'y': y, 'to_x': x - 1, 'to_y': y - 1, 'direction': common.DIAGONAL_FORWARD_LEFT1, 'step': 1,
             'piece_type': piece_type})

    # 전진 길 체크
    if y != 0 and not common.is_our_side(state_map, x, y - 1, side):
        # and not util.is_losing_way(state_map, x, y, x, y - 1, side):
        action_list.append(
            {'x': x, 'y': y, 'to_x': x, 'to_y': y - 1, 'direction': common.FORWARD, 'step': 1, 'piece_type': piece_type})

    # 오른쪽 길 체크
    if x != 8 and not common.is_our_side(state_map, x + 1, y, side):
        # and   not util.is_losing_way(state_map, x, y, x + 1, y, side):
        action_list.append(
            {'x': x, 'y': y, 'to_x': x + 1, 'to_y': y, 'direction': common.RIGHT, 'step': 1, 'piece_type': piece_type})

    # 왼쪽 길 체크
    if x != 0 and not common.is_our_side(state_map, x - 1, y, side):
        # and   not util.is_losing_way(state_map, x, y, x - 1, y, side):
        action_list.append(
            {'x': x, 'y': y, 'to_x': x - 1, 'to_y': y, 'direction': common.LEFT, 'step': 1, 'piece_type': piece_type})

    return action_list