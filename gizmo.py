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
    
    def multiplication_table(self, zero_out_multiples = None):
        a = np.arange(1,13)
        mm = np.outer(a,a)
        if isinstance(zero_out_multiples, int):
            for i in range(1,13):
                if i%zero_out_multiples == 0:
                    mm[(i-1),:] = 0
                    mm[:,(i-1)] = 0
    
        return mm
            
    

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
