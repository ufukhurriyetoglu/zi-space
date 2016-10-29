import numpy as np
import tensorflow as tf
from six.moves import cPickle as pickle

image_size = 44
binary_dim = 64
pickle_file = "simp_jhenghei.pickle"
batch_size = 16
patch_size = 5
depth = 16
num_hidden = 256
alpha = 1

with open(pickle_file, 'rb') as f:
    all_data = pickle.load(f).reshape((-1, image_size, image_size, 1)).astype(np.float32)


graph = tf.Graph()

with graph.as_default():

    x = tf.placeholder(tf.float32, shape=(batch_size, image_size, image_size, 1))

    layer1_weights = tf.Variable(tf.truncated_normal(
        [patch_size, patch_size, 1, depth], stddev=0.1))
    layer1_biases = tf.Variable(tf.zeros([depth]))
    layer2_weights = tf.Variable(tf.truncated_normal(
        [patch_size, patch_size, depth, depth], stddev=0.1))
    layer2_biases = tf.Variable(tf.constant(1.0, shape=[depth]))
    layer3_weights = tf.Variable(tf.truncated_normal(
        [image_size // 4 * image_size // 4 * depth, num_hidden], stddev=0.1))
    layer3_biases = tf.Variable(tf.constant(1.0, shape=[num_hidden]))
    layer4_weights = tf.Variable(tf.truncated_normal(
        [num_hidden, binary_dim], stddev=0.1))
    layer4_biases = tf.Variable(tf.constant(1.0, shape=[binary_dim]))

     # Model.
    def model(data):

        conv = tf.nn.conv2d(data, layer1_weights, [1, 2, 2, 1], padding='SAME')
        hidden = tf.nn.relu(conv + layer1_biases)
        conv = tf.nn.conv2d(hidden, layer2_weights, [1, 2, 2, 1], padding='SAME')
        hidden = tf.nn.relu(conv + layer2_biases)
        shape = hidden.get_shape().as_list()
        reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
        hidden = tf.nn.relu(tf.matmul(reshape, layer3_weights) + layer3_biases)
        return tf.matmul(hidden, layer4_weights) + layer4_biases
        
    def binarize(data):
#        return (0.5 * (np.sign(model(data)) + 1))
         return model(data)

    loss_1 = alpha * tf.nn.l2_loss((binarize(x) - 0.5) - model(x))
    loss = tf.reduce_sum(loss_1)
     
    # Optimizer.
    optimizer = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

num_steps = 1001

with tf.Session(graph=graph) as session:
    tf.initialize_all_variables().run()
    print('Initialized')
    for step in range(num_steps):
        offset = (step * batch_size) % (all_data.shape[0] - batch_size)
        batch_data = all_data[offset:(offset + batch_size), :, :, :]
        feed_dict = {x : batch_data}
        _, l = session.run([optimizer, loss], feed_dict=feed_dict)
        if (step % 50 == 0):
            print(step)
    binary_representation = model(all_data)        

with open('binary.pickle', 'wb') as f:
    pickle.dump(np.asarray(binary_representation), f, pickle.HIGHEST_PROTOCOL)

