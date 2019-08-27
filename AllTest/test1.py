import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]
noise = np.random.normal(0,0.02,x_data.shape)
y_data = np.square(x_data) + noise
#定义中间层
W_L1 = tf.Variable(tf.random_normal([10,200]))
B_L1 = tf.Variable(tf.zeros([10,1]))
Z_L1 = tf.matmul(W_L1,x_data) + B_L1
A_L1 = tf.nn.tanh(Z_L1)

#定义输出层
W_L2 = tf.Variable(tf.random_normal([1,10]))
B_L2 = tf.Variable(tf.zeros([1,1]))
Z_L2 = tf.matmul(W_L2,A_L1) + B_L2
A_L2 = tf.nn.tanh(Z_L2)


#二次代价函数
loss = tf.reduce_mean(tf.square(y_data-A_L2))

#梯度下降法
train_setp = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for step in range(200):
        sess.run(train_setp)

    prediction_value = sess.run(A_L2)

    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction_value,'r-',lw=5)
    plt.show()