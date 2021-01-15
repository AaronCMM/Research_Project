'''模型训练'''
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras import *
import numpy as np
import os
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import Callback
from traindata import X_train,X_test,y_train,y_test
import matplotlib.pyplot as plt

callbacks = [EarlyStopping(monitor='val_loss', verbose=1, patience=1111),
			 ModelCheckpoint("filter_2.hdf5", monitor='val_mean_absolute_error',
							 mode='min', verbose=0, save_best_only=True)]   

def attention_3d_block(inputs):
    input_dim = int(inputs.shape[2]) 

    a = Permute((2, 1))(inputs)          
    a = Reshape((input_dim, 6))(a)  
    a = Dense(6, activation='softmax')(a)
    a_probs = Permute((2, 1), name='attention_vec')(a)
    output_attention_mul = Multiply()([inputs, a_probs])
    return output_attention_mul

inputs = Input(shape=(X_train.shape[1], X_train.shape[2]))    # 6x9
context1 = Bidirectional(LSTM(48, return_sequences=True))(inputs)  
atten = attention_3d_block(context1)
drop=Dropout(0.2)(atten)
atten = Flatten()(drop)    #Flatten层，把多维的输入一维化

x=Dense(64, activation='relu')(atten)
x=Dense(32, activation='relu')(x)
x=Dense(12, activation='relu')(x)

output = Dense(target.shape[1], activation='relu')(x)  
model = Model(inputs=[inputs], outputs=output)
model.compile(loss='mean_squared_error', optimizer='adam',metrics =['mae','mse'])   
model.summary()  

history = model.fit(X_train, y_train, epochs=1200, batch_size=64, callbacks=callbacks,validation_data=( X_test, y_test), verbose=1)

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show() 