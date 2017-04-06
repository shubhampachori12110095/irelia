import tensorflow as tf
from util import neural_network as nn
import numpy as np
import os
from util import gibo_csv_reader as reader
from core import game
import operator

F = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer('num_repeat_layers', 11, 'The number of cnn repeat layers.')
tf.app.flags.DEFINE_integer('num_filters', 192, 'The number of cnn filters.')
tf.app.flags.DEFINE_string('data_format', 'NCHW', 'cnn data format')
tf.app.flags.DEFINE_string('checkpoint_path', '/home/igseo/data/korean_chess/train_log/sl_policy_network.ckpt',
                           'cnn data format')
tf.app.flags.DEFINE_string('state',
                           'r6,r4,r2,r3,1,r3,r2,r4,r6,4,r7,5,r5,5,r5,1,r1,1,r1,1,r1,1,r1,1,r1,18,b1,1,b1,1,b1,1,b1,1,b1,1,b5,5,b5,5,b7,4,b6,b2,b4,b3,1,b3,b4,b2,b6',
                           'current state')

tf.app.flags.DEFINE_string('color', 'b', 'current turn')

width = 9
height = 10
num_input_feature = 3

if F.data_format is 'NCHW':
    inputs = tf.placeholder(tf.float16, [None, num_input_feature, height, width], name='inputs')
else:
    inputs = tf.placeholder(tf.float16, [None, height, width, num_input_feature], name='inputs')

logits, end_points = nn.sl_policy_network(inputs, F.num_repeat_layers, F.num_filters,
                                          data_format=F.data_format)

argmax = tf.argmax(end_points['Predictions'], 2)

init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
sess.run(init)

saver = tf.train.Saver()
saver.restore(sess, F.checkpoint_path)

x_train = game.convert_state_feature_map(F.state, F.color)
if F.data_format is not 'NCHW':
    x_train = np.transpose(x_train, (0, 2, 3, 1))
result, pred = sess.run([argmax, end_points['Predictions']], {inputs: x_train})

before_list = np.argsort(-pred[0][0])
after_list = np.argsort(-pred[0][1])
print(before_list)
print(after_list)
print(pred[0][0][before_list])
print(pred[0][1][after_list])
actions_dict = game.get_actions_hash_map(F.state, F.color)
result_dict = {}
for after_position in after_list:
    to_value = pred[0][1][after_position]
    to_x, to_y = game.convert_one_dim_pos_to_two_dim_pos(after_position)
    for before_position in before_list:
        if before_list[before_position] is False:
            continue
        before_value = pred[0][0][before_position]
        x, y = game.convert_one_dim_pos_to_two_dim_pos(before_position)
        pos_key = game.build_pos_key(x, y, to_x, to_y)
        if pos_key in actions_dict:
            result_dict[pos_key] = before_value + to_value
            before_list[before_position] = False
            break

result_dict = sorted(result_dict.items(), key=operator.itemgetter(1))
result_dict.reverse()
print(result)
print(result_dict)
key_list = [x[0] for x in result_dict]
value_list = [x[1] for x in result_dict]

e = np.exp(np.array(value_list) / 1.0)
probabilities = e / np.sum(e)

sample = np.random.choice(key_list, 1, p=probabilities)
print(value_list)
print(probabilities)
print(sample[0])
