import numpy as np

def __rmspe(y, yhat):
    return np.sqrt(np.mean(np.power(1-(yhat/y),2)))

def rmspe_sqrt_xgb(yhat, y):
    y=np.power(y.get_label(),2)
    yhat = np.power(yhat,2)
    return "rmspe", __rmspe(y, yhat)

def rmspe_sqrt_skl(y, yhat):
    y = np.power(y,2)
    yhat = np.power(yhat,2)
    return __rmspe(y, yhat)

def rmspe_log_xgb(yhat, y):
    y=np.exp(y.get_label())
    yhat = np.exp(yhat)
    return "rmspe", __rmspe(y, yhat)

def rmspe_log_skl(y, yhat):
    y = np.exp(y)
    yhat = np.exp(yhat)
    return __rmspe(y, yhat)



# def rmspe(y, yhat):
#     return np.sqrt(np.mean((yhat/y-1) ** 2))
#
# def rmspe_xg(yhat, y):
#     y = np.expm1(y.get_label())
#     yhat = np.expm1(yhat)
#     return "rmspe", rmspe(y,yhat)
#
# def ToWeight(y):
#     #print(y)
#     w = np.zeros(y.shape, dtype=float)
#     ind = y != 0
#     #print(ind)
#     #print(y[ind]**2)
#     #print(1/y[ind]**2)
#     #print (w[ind])
#     #print(np.where(ind))
#     #w[np.where(ind)] = 1/(y[np.where(ind)]**2)
#     #print(w[ind])
#     w=1/(y**2)
#     return w
#
#
# def xgb_feval_rmspe_sqrt(yhat, y):
#     # y = y.values
#     y = y.get_label()
#     y = np.power(y,2)
#     yhat = np.power(yhat,2)
#     w = ToWeight(y)
#     rmspe = np.sqrt(np.mean(w * (y - yhat)**2))
#     return "rmspe", rmspe
#
# #def sklearn_rmspe_sqrt(estimator, X, y):
# def sklearn_rmspe_sqrt(y, yhat):
#     #yhat=estimator.predict(X)
#     y = np.power(y,2)
#     yhat = np.power(yhat,2)
#     w = ToWeight(y)
#     rmspe = np.sqrt(np.mean(w * (y - yhat)**2))
#     return rmspe

my_variable = 4