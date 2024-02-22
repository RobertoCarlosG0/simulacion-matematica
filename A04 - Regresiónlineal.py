#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_excel("Motor Trend Car Road Tests.xlsx")
data


# In[2]:


data.boxplot()


# In[3]:


data = data.loc[:, data.columna != model]


# In[4]:


columnas = ["mpg", "cyl", "disp", "hp", "drat","wt","qsec","vs","am", "gear", "carb"]
datos_filtrados = data[ columnas ]
datos_filtrados.describe()


# In[5]:


def scaler(variable) :
    variable = variable - min(variable)
    variable = variable/max(variable)
    return variable
datos_filtrados.loc[:,"mpg"] = scaler(datos_filtrados["mpg"])
datos_filtrados.loc[:,"cyl"] = scaler(datos_filtrados["cyl"])
datos_filtrados.loc[:,"disp"] = scaler(datos_filtrados["disp"])
datos_filtrados.loc[:,"hp"] = scaler(datos_filtrados["hp"])
datos_filtrados.loc[:,"drat"] = scaler(datos_filtrados["drat"])
datos_filtrados.loc[:,"wt"] = scaler(datos_filtrados["wt"])
datos_filtrados.loc[:,"qsec"] = scaler(datos_filtrados["qsec"])
datos_filtrados.loc[:,"vs"] = scaler(datos_filtrados["vs"])
datos_filtrados.loc[:,"am"] = scaler(datos_filtrados["am"])
datos_filtrados.loc[:,"gear"] = scaler(datos_filtrados["gear"])
datos_filtrados.loc[:,"carb"] = scaler(datos_filtrados["carb"])

datos_filtrados.describe()


# In[6]:


def funcion_de_costo(beta, X, y) :
    r, c = X.shape
    beta = np.reshape(beta,[c, 1])
    y_pred = X @ beta
    error = y_pred - y
    return (error.T @ error)[0][0]

import numpy as np

m = len(datos_filtrados["mpg"])
ones = np.ones([m, 1])
CYL = np.reshape(datos_filtrados["cyl"],[m, 1])
DISP= np.reshape(datos_filtrados["disp"],[m, 1])
HP= np.reshape(datos_filtrados["hp"],[m, 1])
DRAT= np.reshape(datos_filtrados["drat"],[m, 1])
WT= np.reshape(datos_filtrados["wt"],[m, 1])
QSEC= np.reshape(datos_filtrados["qsec"],[m, 1])
VS= np.reshape(datos_filtrados["vs"],[m, 1])
AM= np.reshape(datos_filtrados["am"],[m, 1])
GEAR= np.reshape(datos_filtrados["gear"],[m, 1])
CARB= np.reshape(datos_filtrados["carb"],[m, 1])


X = np.hstack ((ones, CYL, DISP, HP, DRAT, WT, QSEC, VS, AM, GEAR, CARB))

y = np.reshape(datos_filtrados["mpg"], [m, 1])


# In[8]:


import scipy.optimize as opt

beta = [0, 1, 2, 5, 10, 12, 8, 13, 13, 53, 4]

opt.minimize(funcion_de_costo, beta, args=(X, y))


# In[ ]:




