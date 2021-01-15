'''预测单个值'''
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras import *
import numpy as np
import os
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint,Callback
from tensorflow.keras.models import Model
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from create_traindate import X_train,X_test,y_train,y_test,target

def attention_3d_block(inputs):

    input_dim = int(inputs.shape[2]) 

    a = Permute((2, 1))(inputs)
    a = Reshape((input_dim, X_train.shape[1]))(a) 
    a = Dense(X_train.shape[1], activation='softmax')(a)
    a_probs = Permute((2, 1), name='attention_vec')(a)
    output_attention_mul = Multiply()([inputs, a_probs])
    return output_attention_mul

'''定义当误差为最小时保存最优模型，patience=1111,1111个epoch损失都没有下降那个提前停止
lsym.hdf5为保存的模型名称，monitor为观测值也就是val_loss，mode='min'代表最小的val_loss'''

callbacks = [EarlyStopping(monitor='val_loss', verbose=1, patience=1111),
			 ModelCheckpoint("lsym.hdf5", monitor='val_mean_absolute_error',
							 mode='min', verbose=0, save_best_only=True)]   

inputs = Input(shape=(X_train.shape[1], X_train.shape[2]))
context1 = Bidirectional(LSTM(48, return_sequences=True))(inputs)  #lstm神经元数量为48个 激活函数为relu
#context1=tensorflow.keras.layers.Dropout(0.5)(context1)
atten = attention_3d_block(context1)
con2=Conv1D(48, 3, padding='same')(atten )
atten=tf.keras.layers.GlobalAveragePooling1D()(con2)
atten = Flatten()(atten)
x = Dense(48, activation='relu')(atten)# 连接层,全连接层神经元维度为48
output = Dense(1, activation='relu')(x)  #softmax层  ReLU作激活函数
model = Model(inputs=[inputs ], outputs=output)
model.compile(loss='mean_squared_error', optimizer='adam',metrics =["mae"])   #损失为mse ，优化器为adam
model.summary()  

LSTM = model.fit(X_train, y_train[:,0], epochs=200, batch_size=32, callbacks=callbacks,validation_data=( X_test, y_test[:,0]), verbose=1)