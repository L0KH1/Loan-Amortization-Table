"""
Author: Luke Alli
File name: loan.py
Purpose: This program accepts a loan amount, interest rate, and fixed number of
years as input and outputs a monthly payment schedule for a loan. The program
computes and prints the month number, the principal owed at the beginning of that
month, the principal and interest paid for that month, and the balance owed at
the end of that month. The numbers in the schedule are right-aligned in their
columns, and each column is suitably labeled. The total amount of interest and
the total amount paid is printed after the schedule is printed.
"""

beginningBalance = float(input("Please enter loan amount: "))
rate = float(input("Please enter rate as a percentage: ")) / 100 / 12
yrs = int(input("Please enter the loan term in years: "))

maxTime = yrs * 12
month = 0
totalInt = 0.0

print("%4s%18s%18s%18s%18s" % ("Month", "Interest", \
"Principal Owed","Monthly Payment", "Ending Balance"))

amt = beginningBalance
payment = beginningBalance * (rate/(1 - (1 + rate)**(-maxTime)))
totalPrincipal = 0
totalInterest = 0
while month < maxTime:
    #calculate interest
    interest = amt * rate
    totalInterest += interest
    #calculate monthly principal and add it to total principal
    principal = payment - interest
    totalPrincipal += principal
    #calculate next month's beginning balance
    amt -= principal
    
    month += 1
    print("%4s%18.2f%18.2f%18.2f%18.2f" % (month , interest, principal, \
                                           payment, amt))
    
print("Total interest: $%0.2f" % totalInterest)
print("Total amount paid: $%0.2f" % (totalInterest + totalPrincipal))
