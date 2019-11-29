#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:57:03 2019

@author: kamil
"""

import time
import numpy as np
import pandas as pd
from lshadecnepsin import get_default_params_lshadecnepsin, apply_lshadecnepsin
from jso import get_default_params_jso, apply_jso
import os
import statistics


def run_lshadecnepsin(params):
    
    start = time.time()
    solution, fitness, best_solutions = apply_lshadecnepsin(**params)
    end = time.time()
    time_elapsed = end - start
    
    return fitness, best_solutions, time_elapsed

def run_jso(params):
    
    start = time.time()
    solution, fitness, best_solutions = apply_jso(**params)
    end = time.time()
    time_elapsed = end - start
    
    return fitness, best_solutions, time_elapsed

def get_row_data(params_lshadecnepsin, params_jso, num_of_runs = 25):
    
    fitness_lshadecnepsin = []
    fitness_jso = []
    best_solutions_lshadecnepsin = [[0, 0]] * params_lshadecnepsin['max_evals']
    best_solutions_jso = [[0, 0]] * params_jso['max_evals']
    time_lshadecnepsin = []
    time_jso = []
    for i in range(0, num_of_runs):  
        print(i+1, ' out of ', num_of_runs, 'runs')
        fitness, best_solutions, time_elapsed= run_lshadecnepsin(params_lshadecnepsin)
        fitness_lshadecnepsin.append(fitness)
        time_lshadecnepsin.append(time_elapsed)
        for j in range(0, len(best_solutions)):
            best_solutions_lshadecnepsin[j] = [best_solutions_lshadecnepsin[j][0]+best_solutions[j],
                                         best_solutions_lshadecnepsin[j][1] + 1]
            
        fitness, best_solutions, time_elapsed= run_jso(params_jso)
        fitness_jso.append(fitness)
        time_jso.append(time_elapsed)
        for j in range(0, len(best_solutions)):
            best_solutions_jso[j] = [best_solutions_jso[j][0]+best_solutions[j],
                                         best_solutions_jso[j][1] + 1]
            
    
    mean_best_solutions_lshadecnepsin = []
    
    for i in range(0, len(best_solutions_lshadecnepsin)):
        if best_solutions_lshadecnepsin[i][0] == 0:
            del best_solutions_lshadecnepsin[i : len(best_solutions_lshadecnepsin)]
            break
        
        mean_best_solutions_lshadecnepsin.append(best_solutions_lshadecnepsin[i][0]/best_solutions_lshadecnepsin[i][1])
        
    mean_best_solutions_jso = []
    
    for i in range(0, len(best_solutions_jso)):
        if best_solutions_jso[i][0] == 0:
            del best_solutions_jso[i : len(best_solutions_jso)]
            break
            
        mean_best_solutions_jso.append(best_solutions_jso[i][0]/best_solutions_jso[i][1])
    
    Dict = {} 
    
    Dict['fit_lsh_median'] = statistics.median(fitness_lshadecnepsin)
    Dict['fit_lsh_mean'] = statistics.mean(fitness_lshadecnepsin)
    Dict['fit_lsh_standard_deviation'] = statistics.stdev(fitness_lshadecnepsin)
    Dict['fit_lsh_best'] = min(fitness_lshadecnepsin)
    Dict['time_lsh_mean'] = statistics.mean(time_lshadecnepsin)
    #Dict['mean_best_solutions_lshadecnepsin'] = mean_best_solutions_lshadecnepsin
        
    Dict['fit_jso_median'] = statistics.median(fitness_jso)
    Dict['fit_jso_mean'] = statistics.mean(fitness_jso)
    Dict['fit_jso_standard_deviation'] = statistics.stdev(fitness_jso)
    Dict['fit_jso_best'] = min(fitness_jso)
    Dict['time_jso_mean'] = statistics.mean(time_jso)
    #Dict['mean_best_solutions_jso'] = mean_best_solutions_jso

    
    return Dict, mean_best_solutions_lshadecnepsin, mean_best_solutions_jso
        
        
    
    
    


 
