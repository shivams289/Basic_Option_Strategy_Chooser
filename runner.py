
import pandas as pd
import numpy as np
import math
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from Model.model import Strategy

def wanna_proceed(reply):
    if reply == True:
        Call_strategy()
    else:
        print('Thank you! See you again.')

def take_inputs():
   
    val = input('\nHey! Welcome to Strategy Choosing Program. Please enter your preferences\n\nAre you bullish?:Enter b\nIf bearish:Enter be\nExpect Underlying to be range bound?:Enter r\nIf Expect Either Side Large Moves?:Enter mn\n\n')
    
    return val 

def NameStrat():
    inp = input('Which Strategy you wanna call:\n\nFor put_ratio_back_spread:Enter prbs\nFor call_ratio_back_spread:Enter crbs\nFor bear_put_spread:Enter beps\nFor bear_call_spread:Enter becs\nFor bull_put_spread:Enter bps\nFor bull_call_spread:Enter bcs\nFor long_strangle:Enter lstrg\nFor short_strangle:Enter sstrg\nFor short_straddle:Enter sstrd\nFor long_straddle:Enter lstrd\n')
    
    return inp

def inp_parameters():
    LS = int(input('input lower strike?'))
    HS = int(input('input higher strike?'))
    hsp = int(input('input premium of higher strike?'))
    lsp = int(input('input premium of lower strike?'))
    return LS, HS, hsp, lsp


#---Sentiment---:
#Bullish:b
#bearish:be
#range bound: r
#market neutral: mn

def Call_strategy():
    sentiment = take_inputs()
    if sentiment == 'b':
        print('Bullish Strategies you can call are:\n1.call_ratio_back_spread{if highly bullish}\n2.bull_put_spread(moderately bullish)\n3.bull_call_spread(moderately bullish)\n')
    if sentiment == 'be':
        print('Bearish Strategies you can call are:\n1.put_ratio_back_spread{if highly bullish}\n2.bear_put_spread(moderately bullish)\n3.bear_call_spread(moderately bullish)\n')
    if sentiment == 'r':
        print('Range Bound/Market Neutral Strategies you can call are:\n1.short_straddle\n2.short_strangle')
    if sentiment == 'mn':
        print('Market Neutral Strategies you can call are:\n1.long_straddle\n2.long_strangle')

    inp = NameStrat()
    spot = int(input('Enter Current value of spot?\n'))
    
    if inp == 'prbs':
        print("This Strategy requires you to: Buy 2 OTM PE, Sell an ITM PE\n")
        #take input strategy parameter LS, HS, hsp, lsp, 
        LS, HS, hsp, lsp = inp_parameters()
        prbs = Strategy(LS, spot, HS, hsp, lsp)
        prbs.put_ratio_back_spread()
    if inp == 'crbs':
        print("This Strategy requires you to: Buy 2 OTM CE, Sell ITM CE\n")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        crbs = Strategy(LS, spot, HS, hsp, lsp)
        crbs.call_ratio_back_spread()
        
    if inp == 'beps':
        print("This Strategy requires you to: Buy ITM PE, Sell OTM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        beps = Strategy(LS, spot, HS, hsp, lsp)
        beps.bear_put_spread()
        
    if inp == 'becs':
        print("This Strategy requires you to: Buy OTM CE, Sell ITM CE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        becs = Strategy(LS, spot, HS, hsp, lsp)
        becs.bear_call_spread()
        
    if inp == 'bps':
        print("This Strategy requires you to: Buy OTM PE, Sell ITM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        bps = Strategy(LS, spot, HS, hsp, lsp)
        bps.bull_put_spread()
        
    if inp == 'bcs':
        print("This Strategy requires you to: Buy ITM CE, Sell OTM CE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        bcs = Strategy(LS, spot, HS, hsp, lsp)
        bcs.bull_call_spread()
        
    if inp == 'sstrd':
        print("This Strategy requires you to: Sell ATM CE, Sell ATM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        sstrd = Strategy(LS, spot, HS, hsp, lsp)
        sstrd.short_straddle()
        
    if inp == 'lstrd':
        print("This Strategy requires you to: Buy ATM CE, Buy ATM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        lstrd = Strategy(LS, spot, HS, hsp, lsp)
        lstrd.long_straddle()
        
    if inp == 'sstrg':
        print("This Strategy requires you to: Sell OTM CE, Sell OTM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        sstrg = Strategy(LS, spot, HS, hsp, lsp)
        sstrg.short_strangle()
        
    if inp == 'lstrg':
        print("This Strategy requires you to: Buy OTM CE, Buy OTM PE")
        #take input strategy parameter LS, HS, hsp, lsp,
        LS, HS, hsp, lsp = inp_parameters()
        lstrg = Strategy(LS, spot, HS, hsp, lsp)
        lstrg.long_strangle()

if __name__=='__main__':

    Call_strategy()

    recall = input('Wanna test another strategy?\nif yes: Enter y\nif no: Enter n\n')
    if recall == 'y':
        recall = True
    else:
        recall = False
    wanna_proceed(recall)




