#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras 
import numpy as np


# In[2]:


mnist = tf.keras.datasets.mnist


# In[3]:


(X_train, y_train),(X_test, y_test) = mnist.load_data()


# In[4]:


def relu(x):
    return (x > 0)*x


# In[5]:


def relu_deri(x):
    return x>=0


# In[6]:


images =  X_train[0:60000].reshape(60000,28*28)


# In[7]:


labels = tf.keras.utils.to_categorical(y_train,10)


# In[ ]:


hidden_layer =100
num_class = 10
W_1 = np.random.random((images.shape[1],hidden_layer))
W_2 = np.random.random((hidden_layer,num_class))
for interator in range(100):
    err = 0 
    for (image,label) in zip(images,labels):
        L_0 = image
        L_1 = relu(np.dot(L_0,W_1))
        L_2 =  np.dot(L_1,W_2)
        err += np.sum((label - L_2)**2)
        L_2_delta = (label -L_2)
        L_1_delta = L_2_delta.dot(W_2.T)*relu_deri(L_1)
        print(L_2_delta.T)
        #W_2 += 
        #W_1 += L_0.T.dot(L_1_delta)
    print(err)


# In[24]:


images.shape


# In[26]:


labels.shape


# In[41]:


a = np.array([[2,2],[2,3]])
b = np.array([3,3])
c = a.dot(b)
print(c.dot(b.T))


# In[ ]:




