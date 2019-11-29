#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:34:16 2019

@author: kamil
"""
import os
from compare_functions import get_row_data
from fun_vis import fun_vis
import numpy as np
import matplotlib.pyplot as plt
from jso import get_default_params_jso
from lshadecnepsin import get_default_params_lshadecnepsin
import pandas as pd

#funkcja 1
fun = lambda x: x[0]**5-25*x[0]**3+x[1]**5-25*x[1]**3+400+30*(x[0]**2)*x[1]
bounds = np.array([[-3, 2], [-4.2, 5]]) 

#funkcja 2
'''fun = lambda x: (x[0]**2)*(4-2.1*(x[0]**2)+(x[0]**4)/3)+x[0]*x[1]+(x[1]**2)*(-4 +4*(x[1]**2))
bounds = np.array([[-2.5, 2.5], [-1.5, 1.5]]) '''


#defaultowe parametry dla 2 algorytmow
params_lshadecnepsin = get_default_params_lshadecnepsin(dim = 2)
params_jso = get_default_params_jso(dim = 2)

#funkcja i granice obszaru w ktorym szukamy ekstremum przekazane do parametrow algorytmu lshadecnepsin
params_lshadecnepsin['bounds'] = bounds
params_lshadecnepsin['func'] = fun

#funkcja i granice obszaru w ktorym szukamy ekstremum przekazane do parametrow algorytmu jso
params_jso['bounds'] = bounds
params_jso['func'] = fun

#nie defaultowa populacj
#params_lshadecnepsin['population_size'] = 30
#params_jso['population_size'] = 30


#Dict zawiera wszystkie wartosci ktore nalezy wpisac do wiersza tabeli
#pozostale dwie zmienne zwracane przez funkcje to lista najlepszych osobnikow z danej generacji dla 
#algorytmow lshadecnepsin i jso
Dict = {} 

#%%

#Pierwszy wiersz

Dict, mean_best_solutions_lshadecnepsin, mean_best_solutions_jso = get_row_data(params_lshadecnepsin, params_jso)

x = np.arange(0., len(mean_best_solutions_lshadecnepsin), 1)

plt.scatter(x, mean_best_solutions_lshadecnepsin, label= "lsh", color= "green",  
            marker= "*", s=30) 

x = np.arange(0., len(mean_best_solutions_jso), 1)

plt.scatter(x, mean_best_solutions_jso, label= "lsh", color= "red",  
            marker= "^", s=30) 

plt.title('Krzywa zbieznosci dla funkcji 1')
plt.xlabel('pokolenia') 
plt.ylabel('wartosc funkcji celu') 

plt.legend() 

plt.savefig('plot.png')

plt.show()



df = pd.DataFrame(Dict, index=[0])

#%%

#Drugi wiersz

fun = lambda x: (x[0]**2)*(4-2.1*(x[0]**2)+(x[0]**4)/3)+x[0]*x[1]+(x[1]**2)*(-4 +4*(x[1]**2))
bounds = np.array([[-2.5, 2.5], [-1.5, 1.5]])
params_lshadecnepsin['bounds'] = bounds
params_lshadecnepsin['func'] = fun
params_jso['bounds'] = bounds
params_jso['func'] = fun
Dict, mean_best_solutions_lshadecnepsin, mean_best_solutions_jso = get_row_data(params_lshadecnepsin, params_jso)


df = df.append(Dict, ignore_index=True)

with open("df.txt", "w") as text_file:
    text_file.write(df.to_string())


