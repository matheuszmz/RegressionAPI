
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[2]:


path = os.getcwd()[:os.getcwd().find('models')]
data = pd.read_json(path + 'cetano.json')


# In[3]:


X = data[['C8:0', 'C10:0', 'C12:0', 'C14:0', 'C16:0','C18:0', 'C18:1', 'C18:2', 'C18:3', 'C18:1 OH', 'C20:0', 'C20:1', 'C22:1', 'Outros']]
Y = data['NC']


# In[4]:


from sklearn.model_selection import train_test_split
from sklearn import metrics


# In[5]:


def metrics_calc (Y_test, predict):
    print('R²  : ', metrics.r2_score(Y_test, predict))
    print('MAE : ', metrics.mean_absolute_error(Y_test, predict))
    print('MSE : ', metrics.mean_squared_error(Y_test, predict))
    print('RMSE: ', np.sqrt(metrics.mean_squared_error(Y_test, predict)))


# ## Partial least squares regression (PLS regression) 

# In[6]:


from sklearn.cross_decomposition import PLSRegression


# In[7]:


def regression_pls (X=X, Y=Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=1589078)
    PLS = PLSRegression(n_components=2)
    PLS.fit(X_train, Y_train)
    PLS_predict = PLS.predict(X_test)
    return Y_test, PLS_predict


# In[8]:


Y_test, PLS_predict = regression_pls()
metrics_calc(Y_test, PLS_predict)


# ## Multiple Linear Regression - MLR

# In[9]:


from sklearn.linear_model import LinearRegression


# In[10]:


def regression_mlr (X=X, Y=Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=233080)
    MLR = LinearRegression()
    MLR.fit(X_train, Y_train)
    MLR_predict = MLR.predict(X_test)
    return Y_test, MLR_predict


# In[11]:


Y_test, MLR_predict = regression_mlr()
metrics_calc(Y_test, MLR_predict)


# ## Support Vector Regression - SVR

# In[12]:


from sklearn.svm import LinearSVR


# In[13]:


def regression_svr (X=X, Y=Y, random_state=0):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=1384793)
    SVR = LinearSVR(random_state=52920)
    SVR.fit(X_train,Y_train)
    SVR_predict = SVR.predict(X_test)
    return Y_test, SVR_predict


# In[14]:


Y_test, SVR_predict = regression_svr(random_state=1)
metrics_calc(Y_test, SVR_predict)


# ## Exportando resultados

# In[19]:


PLS_data = pd.DataFrame(PLS_predict)
PLS_data.to_excel('PLS_predict.xlsx')
MLR_data = pd.DataFrame(MLR_predict)
MLR_data.to_excel('MLR_predict.xlsx')
SVR_data = pd.DataFrame(SVR_predict)
SVR_data.to_excel('SVR_predict.xlsx')

