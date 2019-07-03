import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR

data = pd.read_json('cetano.json')
X = data[['C8:0', 'C10:0', 'C12:0', 'C14:0', 'C16:0','C18:0', 'C18:1', 'C18:2', 'C18:3', 'C18:1 OH', 'C20:0', 'C20:1', 'C22:1', 'Outros']]
Y = data['NC']

def regression_pls (x_test, X=X, Y=Y):
    X_train, X_TEST, Y_train, Y_TESTE = train_test_split(
        X, Y, test_size=0.4, random_state=1589078
        )
    x_test = pd.DataFrame([x_test for i in range(len(X_TEST))])
    PLS = PLSRegression(n_components=2)
    PLS.fit(X_train, Y_train)
    PLS_predict = PLS.predict(x_test)
    return Y_TESTE, PLS_predict

def regression_mlr (x_test, X=X, Y=Y):
    X_train, X_TEST, Y_train, Y_TESTE = train_test_split(
        X, Y, test_size=0.4, random_state=233080
        )
    x_test = pd.DataFrame([x_test for i in range(len(X_TEST))])
    MLR = LinearRegression()
    MLR.fit(X_train, Y_train)
    MLR_predict = MLR.predict(x_test)
    return Y_TESTE, MLR_predict

def regression_svr (x_test, X=X, Y=Y):
    X_train, X_TEST, Y_train, Y_TESTE = train_test_split(
        X, Y, test_size=0.4, random_state=1384793
        )
    x_test = pd.DataFrame([x_test for i in range(len(X_TEST))])
    SVR = LinearSVR(random_state=52920)
    SVR.fit(X_train,Y_train)
    SVR_predict = SVR.predict(x_test)
    return Y_TESTE, SVR_predict
    
def metrics_calc (Y_test, predict):
    #return R², MAE, MSE, RMSE
    return (metrics.r2_score(Y_test, predict),
    metrics.mean_absolute_error(Y_test, predict),
    metrics.mean_squared_error(Y_test, predict),
    np.sqrt(metrics.mean_squared_error(Y_test, predict)))
