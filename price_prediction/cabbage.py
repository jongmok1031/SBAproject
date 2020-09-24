import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from util.file_handler import FileReader
import pandas as pd
import numpy as np
import tensorflow as tf

# entity랑 서비스 합칠꺼야 모델로
class Model:
    def __init__(self):
        self.fileReader = FileReader()
    def new_model(self, payload):
        this = self.fileReader
        this.context = '/Users/jongm/SBAprojects/price_prediction/data/'
        this.fname = payload 
        return pd.read_csv(this.context + this.fname, sep = ',')

    def create_tf(self,payload):
        xy= np.array(payload, dtype = np.float32)
        x_data = xy[:,1:-1] # feature
        y_data = xy[:,[-1]] # label
        X = tf.placeholder(tf.float32, shape=[None,4])
        Y = tf.placeholder(tf.float32, shape = [None,1])
        W = tf.Variable(tf.random_normal([4,1]), name = 'weight')
        b = tf.Variable(tf.random_normal([1]), name = 'bias')
        hypothesis = tf.matmul(X,W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        for step in range(100000):
            cost_, hypo_, = sess.run([cost, hypothesis, train], feed_dict = {X:x_data, Y:y_data})
            if step % 500 == 0:
                print(f'# {step} 손실비용: {cost_}')    
                print(f'- 배추가격 : {hypo_[0]}')
        
        saver = tf.train.Saver()
        print('저장완료')

print('as')