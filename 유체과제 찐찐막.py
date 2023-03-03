# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.xscale('symlog')
def f(x):
    return x
def g(x):
    return 2.44*np.log(x)+5.0
def h(x):
    return x
def a(x):
    return 2.44*np.log(x)+5.0
def b(x):
    return 2.44*np.log(x)+5.0
t1 = np.arange(0,5,0.1)
t2 = np.arange(30,1500,0.1)
t3 = np.arange(5,20)
t4 = np.arange(5,30)
t5 = np.arange(1500,12000)
plt.axis([0,100000,0,40])
plt.plot(t1,f(t1),t2,g(t2),t3,h(t3),'b--', t4,a(t4),'r--',t5,b(t5),'g--')
plt.xlabel("u*y/v")
plt.ylabel("u/u*")
font1 = {'size': 8}
font2 = {'size': 9}
plt.text(0.3,22, 'Viscous sublayer', fontdict=font1)
plt.text(50,29, ' Overlap layer', fontdict=font2)
plt.axvline(5,0.12,0.53, color='lightgray',linestyle='--', linewidth=1)
plt.axhline(21, 0, 0.26, color='lightgray', linestyle='solid', linewidth=1)
plt.axvline(30,0.33,0.7, color='lightgray',linestyle='--', linewidth=1)
plt.axhline(28, 0.393, 0.686, color='lightgray', linestyle='solid', linewidth=1)
plt.axvline(1500,0.57,0.7, color='lightgray',linestyle='--', linewidth=1)
plt.savefig('hi2', dpi=500)
plt.show()

