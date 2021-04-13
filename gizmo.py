#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:26:42 2021

@author: arsii
"""

import numpy as np

class Gizmo:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print(f'{self.name}')
    
    def multiplication_table(self):
        a = np.arange(1,13)
        return np.outer(a,a)

def hello(name, country='Finland'):
	print(f'Hello {name}, how are things in {country}?')
	
def spell(word):
    
    for i in range(len(word)):
        if i < len(word) -1:
            print(word[i], end='.')
        else:
            print(word[i],end='')
            
    print("\n")
    	
def relative_path(subjects):
    return [f'./subjects/mock_recording_{i}.rec' for i in subjects]
