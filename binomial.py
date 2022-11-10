# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:21:24 2022

@author: Richa
"""

from scipy.stats import binomtest

confidence = 0.95
print("Assume 95% confidence")
percent = float(input("Goal is ?%: "))/100.0

trials = 20
fails = 1
while(trials < 10000 and fails < 10):
    trials = trials + 1
    tt = binomtest(trials-fails, trials, percent, alternative='less')
    if(tt.pvalue>confidence):
        print("{}/{}, P-Value: {:.2}".format(fails, trials, tt.pvalue))
        fails = fails + 1