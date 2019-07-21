# -*- coding: utf-8 -*-
"""Energy Disaggregation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s8acrJn9hzZYTt0FAi4mbvO0p4zeXmGd
"""

from google.colab import drive
drive.mount('/content/gdrive')

# %cd gdrive/'My Drive'/'Low rate Energy/low_freq'

HOUSE_1='house_1/'
HOUSE_2='house_2/'
HOUSE_3='house_3/'
HOUSE_4='house_4/'
HOUSE_5='house_5/'
HOUSE_6='house_6/'

import pandas as pd
import numpy as np
from keras.models import Model
from keras.layers import Input,Dense,Conv1D,MaxPooling1D,Flatten,Concatenate
from tqdm import tqdm_notebook as tqdm
from keras.callbacks import ReduceLROnPlateau

label_house1=pd.read_csv(HOUSE_1+'labels.csv',sep=' ',header=None)
label_house1_list=list(label_house1.iloc[:,1])
label_house2=pd.read_csv(HOUSE_2+'labels.csv',sep=' ',header=None)
label_house2_list=list(label_house2.iloc[:,1])
label_house3=pd.read_csv(HOUSE_3+'labels.csv',sep=' ',header=None)
label_house3_list=list(label_house3.iloc[:,1])
label_house4=pd.read_csv(HOUSE_4+'labels.csv',sep=' ',header=None)
label_house4_list=list(label_house4.iloc[:,1])
label_house5=pd.read_csv(HOUSE_5+'labels.csv',sep=' ',header=None)
label_house5_list=list(label_house5.iloc[:,1])
label_house6=pd.read_csv(HOUSE_6+'labels.csv',sep=' ',header=None)
label_house6_list=list(label_house6.iloc[:,1])

label_house1_list

label_house2_list

label_house3_list

label_house4_list

label_house5_list

label_house6_list

appliances=['kitchen_outlets','washer_dryer','lighting','dishwasher']

dishwasher_house1=np.array(pd.read_csv(HOUSE_1+'channel_6.csv',sep=' ',header=None))
dishwasher_house2=np.array(pd.read_csv(HOUSE_2+'channel_10.csv',sep=' ',header=None))
dishwasher_house3=np.array(pd.read_csv(HOUSE_3+'channel_9.csv',sep=' ',header=None))
dishwasher_house4=np.array(pd.read_csv(HOUSE_4+'channel_15.csv',sep=' ',header=None))
dishwasher_house5=np.array(pd.read_csv(HOUSE_5+'channel_20.csv',sep=' ',header=None))
dishwasher_house6=np.array(pd.read_csv(HOUSE_6+'channel_9.csv',sep=' ',header=None))
dishwasher_house1

mains1_house1=np.array(pd.read_csv(HOUSE_1+'channel_1.csv',sep=' ',header=None))
mains2_house1=np.array(pd.read_csv(HOUSE_1+'channel_2.csv',sep=' ',header=None))
mains1_house2=np.array(pd.read_csv(HOUSE_2+'channel_1.csv',sep=' ',header=None))
mains2_house2=np.array(pd.read_csv(HOUSE_2+'channel_2.csv',sep=' ',header=None))
mains1_house3=np.array(pd.read_csv(HOUSE_3+'channel_1.csv',sep=' ',header=None))
mains2_house3=np.array(pd.read_csv(HOUSE_3+'channel_2.csv',sep=' ',header=None))
mains1_house4=np.array(pd.read_csv(HOUSE_4+'channel_1.csv',sep=' ',header=None))
mains2_house4=np.array(pd.read_csv(HOUSE_4+'channel_2.csv',sep=' ',header=None))
mains1_house5=np.array(pd.read_csv(HOUSE_5+'channel_1.csv',sep=' ',header=None))
mains2_house5=np.array(pd.read_csv(HOUSE_5+'channel_2.csv',sep=' ',header=None))
mains1_house6=np.array(pd.read_csv(HOUSE_6+'channel_1.csv',sep=' ',header=None))
mains2_house6=np.array(pd.read_csv(HOUSE_6+'channel_2.csv',sep=' ',header=None))

mains_house1=[[val[0][0],val[0][1],val[1][1]] for val in tqdm(zip(mains1_house1,mains2_house1)) if val[0][0] in dishwasher_house1[:,0]]

mains_house2=[[val[0][0],val[0][1],val[1][1]] for val in tqdm(zip(mains1_house2,mains2_house2)) if val[0][0] in dishwasher_house2[:,0]]
mains_house3=[[val[0][0],val[0][1],val[1][1]] for val in tqdm(zip(mains1_house3,mains2_house3)) if val[0][0] in dishwasher_house3[:,0]]
mains_house4=[[val[0][0],val[0][1],val[1][1]] for val in tqdm(zip(mains1_house4,mains2_house4)) if val[0][0] in dishwasher_house4[:,0]]
mains_house5=[[val[0][0],val[0][1],val[1][1]] for val in tqdm(zip(mains1_house5,mains2_house5)) if val[0][0] in dishwasher_house5[:,0]]
mains_house6=[[val[0][0],val[0][1],val[1][1]] for val in tqdm(zip(mains1_house6,mains2_house6)) if val[0][0] in dishwasher_house6[:,0]]

import pickle
pickle_out = open("main1.pickle","wb")
pickle.dump(mains_house1, pickle_out)
pickle_out.close()
pickle_out = open("main2.pickle","wb")
pickle.dump(mains_house2, pickle_out)
pickle_out.close()
pickle_out = open("main3.pickle","wb")
pickle.dump(mains_house3, pickle_out)
pickle_out.close()
pickle_out = open("main4.pickle","wb")
pickle.dump(mains_house4, pickle_out)
pickle_out.close()
pickle_out = open("main5.pickle","wb")
pickle.dump(mains_house5, pickle_out)
pickle_out.close()
pickle_out = open("main6.pickle","wb")
pickle.dump(mains_house6, pickle_out)
pickle_out.close()

import pickle
pickle_in = open("main1.pickle","rb")
mains_house1 = pickle.load(pickle_in)

main_time_series=[var[0] for var in mains_house1]
modified_dishwasher_house1=[var for var in tqdm(dishwasher_house1) if var[0] in main_time_series]

pickle_out = open("dishwasher.pickle","wb")
pickle.dump(modified_dishwasher_house1, pickle_out)
pickle_out.close()

pickle_in = open("dishwasher.pickle","rb")
modified_dishwasher_house1 = pickle.load(pickle_in)

print(len(modified_dishwasher_house1))
print(len(mains_house1))

mains1=[]
mains2=[]
for i in mains_house1:
  mains1.append(i[1])
  mains2.append(i[2])

X_train=np.zeros((len(mains_house1)-500,499,499))
y_train=np.zeros((len(mains_house1)-500,1))

for i in range(1,len(mains_house1)-500):
  temp1=mains1[i:i+499]
  temp2=mains2[i:i+499]
  temp=[temp1,temp2]
  X_train[i]=temp

diff_mains1=[]
diff_mains2=[]
X_diff=np.zeros((len(mains_house1)-500,499,499))

for i in range(1,len(mains_house1)):
  diff_mains1.append(mains1[i]-mains1[i-1])
  diff_mains2.append(mains2[i]-mmains2[i-1])
  
for i in range(1,len(mains_house1)-500):
  temp1=diff_mains1[i:i+499]
  temp2=diff_mains2[i:i+499]
  temp=np.array(temp1,temp2)
  X_diff[i]=temp

for i in range(1,len(mains_house1)):
  y_train[i]=modified_dishwasher[(i+499)/2][1]

a_input=Input(shape=(499,499,),name='Normal_Input')
a=Conv1D(filters=30,kernel_size=10,activation='relu')(a_input)
a=Conv1D(filters=30,kernel_size=8,activation='relu')(a)
a=Conv1D(filters=40,kernel_size=6,activation='relu')(a)
a=Conv1D(filters=50,kernel_size=5,activation='relu')(a)
a=Conv1D(filters=50,kernel_size=5,activation='relu')(a)
a=Flatten()(a)
a=Dense(1024,activation='relu')(a)

b_input=Input(shape=(499,499,),name='Differential_Input')
b=Conv1D(filters=20,kernel_size=7,activation='relu')(b_input)
b=MaxPooling1D(pool_size=2,strides=2,padding='same')(b)
b=Conv1D(filters=20,kernel_size=7,activation='relu')(b)
b=MaxPooling1D(pool_size=2,strides=2,padding='same')(b)
b=Conv1D(filters=20,kernel_size=5,activation='relu')(b)
b=MaxPooling1D(pool_size=2,strides=2,padding='same')(b)
b=Conv1D(filters=20,kernel_size=5,activation='relu')(b)
b=MaxPooling1D(pool_size=2,strides=2,padding='same')(b)
b=Conv1D(filters=40,kernel_size=3,activation='relu')(b)
b=MaxPooling1D(pool_size=2,strides=2,padding='same')(b)
b=Flatten()(b)
b=Dense(1024,activation='relu')(b)

c=Concatenate()([b,a])
c=Dense(1024,activation='relu')(c)
c=Dense(512,activation='relu')(c)
output=Dense(1,activation='linear',name='Value')(c)

model=Model(inputs=[a_input,b_input],outputs=output)



model.summary()

from keras.utils import plot_model
plot_model(model, to_file='model.png')

reduce_lr = ReduceLROnPlateau(monitor='acc', factor=0.2,
                              patience=5, min_lr=0.0001)
model.fit(x=[X_train,X_diff],y_train,epochs=64)