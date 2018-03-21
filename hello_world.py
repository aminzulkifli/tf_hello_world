import tensorflow as tf
hello = tf.constant('Hello, Tensor flow')
sess = tf.Session()
print(sess.run(hello))