# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:46:38 2022

@author: dreynolds18

Formula:
    PV = Pmt/rDec*(1 - (1+rDec)**(-n)

Problem:
    Now suppose you know you can afford some Pmt amount/month.   Input the interest rate (APR), the number of months  to have for paying back the loan.  Write a program that takes as input:

    1. monthly payment, Pmt

    2 the interest rate (APR)

    3 the number of months to pay back the loan

    Compute the PV, that is, how much you can afford to borrow
"""
import numpy as np

Pmt = float(input('input payment -> '))

rAPR = float(input('input intrest rate, APR -> '))
rDEC = rAPR/1200 # 1200 because monthly pmts
nMonths = int(input('number of months to pay off -> '))

PV = Pmt/rDEC*(1 - (1+rDEC)**(-nMonths))

print(f"for APR={rAPR :.2f}, Pmt = {Pmt :.2f}, number of months = {nMonths :d}")
print(f"Amount you can borrow is {PV :.2f}")

if PV < 20000:
    print('sorry, you gotta buy a used car')
elif PV < 30000:
    print('you can get a Kia Seltos')
else:
    print("you got enough $$ for a Tesla")

