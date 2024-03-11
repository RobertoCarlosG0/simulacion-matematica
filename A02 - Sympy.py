#!/usr/bin/env python
# coding: utf-8

# # Ejercicios de optimización escalar
# ## Roberto Carlos Guzmán Orduño

# **Para la siguientes funciones encuentre los puntos críticos, grafique y diga si éste se trata de un máximo o mínimo, local o global.**

# $f(x)=1260+117x-9x^2$

# In[2]:


import sympy as sp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x = sp.var("x")

def f(x):
    return 1260+117*x-9*x**2

dy=sp.diff(f(x),x)
d2y=sp.diff(dy,x)

pc=sp.solve(dy,x)
opt=f(pc[0])
pc, opt


# In[3]:


d2y.subs(x,pc[0])


# In[6]:


import numpy as np

x_n=np.linspace(-15,20,1000)
y_n=f(x_n)
plt.figure() 
plt.plot(x_n, y_n)
plt.grid()
plt.plot(13/2,6561/4,ms=10)


# In[8]:


respuesta=d2y.subs(x,pc)
if respuesta < 0:
    print("Máximo")
if respuesta > 0:
    print("Minimo")


# $f(x)=5+x+\frac{4}{x}$, para $x>0$

# In[10]:


import sympy as sp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x= sp.var("x")



def f(x):
    return 5+x+4/x

dy=sp.diff(f(x),x)
d2y=sp.diff(dy,x)

pc=sp.solve(dy,x)
opt=f(pc[1])
pc, opt


# In[11]:


d2y.subs(x,pc[1])


# In[12]:


import numpy as np
x_n=np.linspace(0.1,50,1000)

y_n=f(x_n)
plt.figure() 
plt.plot(x_n, y_n)
plt.grid()
plt.plot(2,9,"*r",ms=10)


# In[13]:


respuesta=d2y.subs(x,pc[1])
if respuesta < 0:
    print("Maximo")
if respuesta > 0:
    print("Minimo")


# $f(x)=6-2x+\sqrt{18-2x^2}$, para $-3\leq x\leq 3$

# In[15]:


x= sp.var("x")
def f(x):
    return 6-2*x+(18-2*x**2)**(1/2)
dy=sp.diff(f(x),x)
d2y=sp.diff(dy,x)


# In[17]:


pc=sp.solve(dy,x)
opt=f(pc[0])
pc, opt


# In[18]:


xn=np.linspace(-3,3,100)
yn=f(xn)
plt.figure()
plt.plot(xn,yn)
plt.grid()
plt.plot(pc,opt,"*r",ms=10)


# In[23]:


respuesta=d2y.subs(x,pc[0])
if respuesta < 0:
    print("Máximo")
if respuesta > 0:
    print("Minimo")


# $f(x)=\frac{1}{4}x^4+\frac{1}{3}x^3-x^2$ en el intervalo $[-3,1.7]$

# In[29]:


x= sp.var("x")
def f(x):
    return (1/4*x**4)+(1/3*x**3)-x**2
dy,d2y=sp.diff(f(x),x),sp.diff(dy,x)


# In[30]:


pc, opt_val=sp.solve (dy,x),[]
for p in pc:
    p_ordenado=[p,f(p)]
    opt_val.append(p_ordenado)
opt_val


# In[31]:


xn= np.linspace (-3,1.7,100)
yn=f(xn)
plt.figure()
plt.plot(xn,yn)
plt.grid()
plt.plot(-2.00000000000000,-2.66666666666667,"*r",ms=10)
plt.plot(0,0,"*r",ms=10)
plt.plot(1.00000000000000, -0.416666666666667,"*r",ms=10)


# In[32]:


for p in pc:
    respuesta=d2y.subs(x,p)
    if respuesta < 0:
        print("Máximo")
    if respuesta > 0:
        print("Minimo")
        


# ---
# **Resuelva los siguientes problemas usando la librería `SymPy`. Use celdas en `Markdown` para explicar su procedimiento.**

# El perímetro de un triángulo isósceles es de $10 cm$. ¿Cuánto deben medir sus lados para que el volumen del cuerpo generado por la rotación del triángulo en torno a su base sea el mayor posible? (Volumen de un cono $= \frac{1}{3}\pi r^2 h$, donde $r$ es el radio de la base y $h$ la altura del cono).

# In[33]:


import sympy as sp
r,h,l,b=sp.var("r"),sp.var("h"),sp.var("l"),sp.var("b")
def V(r,h):
    return sp.pi*r**2*h/3
V(r,h)


# In[34]:


res=b+2*l-10
R=b/2
pitagoras=l**2-r**2-h**2


# In[35]:


H=sp.solve(pitagoras,h)[1]
H


# In[36]:


V(r,h).subs(h,H).subs(r,R)


# In[37]:


l_sol=sp.solve(res,l)[0]
l_sol


# In[38]:


V_b=V(r,h).subs(l,l_sol).subs(h,H).subs(r,R)
V_b


# In[39]:


dV=sp.diff(V_b,b)
sp.solve(dV,b)


# In[40]:


l_sol.subs(b,l_sol.subs(b,4))


# In[ ]:





# Disponemos de una barra de aluminio de 6 metros para construir una portería de fútbol. Si queremos que el área de la portería sea máxima, ¿cuánto deben medir los postes y el travesaño?

# In[41]:


import sympy as sp
x, y=sp.var("x"),sp.var("y")
def A(x,y):
    return x*y
res=x+2*y-6
res


# In[42]:


x_y=sp.solve(res,x)[0]
#Usamos el indice 0 para indicar que se usa el valor positivo por la logica del problema

A_y=A(x,y).subs(x,x_y)
dA=sp.diff(A_y,y)
postes=sp.solve(dA,y)[0]
postes


# In[44]:


result=x_y.subs(y,postes)
result


# In[ ]:





# In[ ]:




