#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:26:42 2021

@author: arsii
"""

def hello(name, country='Finland'):
	print(f'Hello {name}, how are things in {country}?')
	
def spell(word):
    for i in word:
        print(i, end='.')
    print("\n")
    	
def relative_path(subjects):
    return [f'./subjects/mock_recording_{i}.rec' for i in subjects]
