
import pandas as pd
import numpy as np
import math
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from Model.model import Strategy

x1 = 'call_ratio_back_spread'
x2 = 'bull_put_spread'
x3 = 'bull_call_spread'

x4 = 'put_ratio_back_spread'
x5 = 'bear_put_spread'
x6 = 'bear_call_spread'

x7 = 'short_straddle'
x8 = 'short_strangle'

x9 = 'long_straddle'
x10 = 'long_strangle'

def wanna_proceed():
    reply = input('\nWanna test another strategy?\nIf yes: Enter y\nElse: Enter n\n')
    if reply == 'n':
        return 'Thank you! See you again.\n'

    return Call_strategy()
    
def take_inputs():
   
    val = input('\nHey! Welcome to Strategy Choosing Program. Please enter your preferences\n\nAre you bullish?:Enter b\nIf bearish:Enter be\nExpect Underlying to be range bound?:Enter r\nIf Expect Either Side Large Moves?:Enter mn\n\n')
    
    return val 

def NameStrat(x, y, z):
    if z == False:
        inp = int(input(f'\nWhich Strategy you wanna call?:\n1.{x}\tEnter 1\n2.{y}\tEnter 2\n'))
    else:
        inp = int(input(f'\nWhich Strategy you wanna call?:\n1.{x}\tEnter 1\n2.{y}\tEnter 2\n3.{z}\tEnter 3\n'))
    
    return inp

def inp_parameters(LS, HS, spot):
    if LS == False and HS == False:
        LS = spot
        HS = spot
    else:
        LS = int(input('input lower strike?\t'))
        HS = int(input('input higher strike?\t'))

    hsp = int(input('input premium of higher strike?\t'))
    lsp = int(input('input premium of lower strike?\t'))
    return LS, HS, hsp, lsp


#---Sentiment---:
#Bullish:b
#bearish:be
#range bound: r
#market neutral: mn

def Call_strategy():
    sentiment = take_inputs()
    if sentiment == 'b':
        print(f'\nBullish Strategies you can call are:\n1.{x1}(Highly bullish)\n2.{x2}(Moderately bullish)\n3.{x3}(Moderately bullish)\n')
        inp = NameStrat(x1, x2, x3)
        spot = int(input('Enter Current value of spot?\t'))
        print('\n')

        if inp == 1:
            print("This Strategy requires you to: Buy 2 OTM CE, Sell ITM CE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            crbs = Strategy(LS, spot, HS, hsp, lsp)
            crbs.call_ratio_back_spread()

        if inp == 2:
            print("This Strategy requires you to: Buy OTM PE, Sell ITM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            bps = Strategy(LS, spot, HS, hsp, lsp)
            bps.bull_put_spread()

        if inp == 3:
            print("This Strategy requires you to: Buy ITM CE, Sell OTM CE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            bcs = Strategy(LS, spot, HS, hsp, lsp)
            bcs.bull_call_spread()

    if sentiment == 'be':
        print(f'\nBearish Strategies you can call are:\n1.{x4}(Highly bearish)\n2.{x5}(Moderately bullish)\n3.{x6}(Moderately bullish)\n')
        inp = NameStrat(x4, x5, x6)
        spot = int(input('Enter Current value of spot?\t'))
        print('\n')

        if inp == 1:
            print("This Strategy requires you to: Buy 2 OTM PE, Sell an ITM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp, 
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            prbs = Strategy(LS, spot, HS, hsp, lsp)
            prbs.put_ratio_back_spread()

        if inp == 2:
            print("This Strategy requires you to: Buy ITM PE, Sell OTM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            beps = Strategy(LS, spot, HS, hsp, lsp)
            beps.bear_put_spread()
        
        if inp == 3:
            print("This Strategy requires you to: Buy OTM CE, Sell ITM CE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            becs = Strategy(LS, spot, HS, hsp, lsp)
            becs.bear_call_spread()

    if sentiment == 'r':
        print(f'\nRange Bound/Market Neutral Strategies you can call are:\n1.{x7}\n2.{x8}\n')
        inp = NameStrat(x7, x8, False)
        spot = int(input('Enter Current value of spot?\t'))
        print('\n')

        if inp == 1:
            print("This Strategy requires you to: Sell ATM CE, Sell ATM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(False, False, spot)
            sstrd = Strategy(LS, spot, HS, hsp, lsp)
            sstrd.short_straddle()

        if inp == 2:
            print("This Strategy requires you to: Sell OTM CE, Sell OTM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            sstrg = Strategy(LS, spot, HS, hsp, lsp)
            sstrg.short_strangle()

    if sentiment == 'mn':
        print(f'\nMarket Neutral Strategies you can call are:\n1.{x9}\n2.{x10}\n')
        inp = NameStrat(x9, x10, False)
        spot = int(input('Enter Current value of spot?\t'))
        print('\n')

        if inp == 1:
            print("This Strategy requires you to: Buy ATM CE, Buy ATM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(False, False, spot)
            lstrd = Strategy(LS, spot, HS, hsp, lsp)
            lstrd.long_straddle()

        if inp == 2:
            print("This Strategy requires you to: Buy OTM CE, Buy OTM PE\n")
            #take input strategy parameter LS, HS, hsp, lsp,
            LS, HS, hsp, lsp = inp_parameters(True, True, spot)
            lstrg = Strategy(LS, spot, HS, hsp, lsp)
            lstrg.long_strangle()

    
    
if __name__=='__main__':

    Call_strategy()
    wanna_proceed()




