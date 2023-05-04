from forex_python.converter import CurrencyRates
cr=CurrencyRates()
amount= int(input("please enter the amount"))
from_currency = input("enter currency code that has to be converted ").upper()
to_currency= input("enter crrency code to convert ").upper()
print("You are converting ", amount,from_currency , "to " , to_currency , ".")
output= cr.convert(from_currency, to_currency,amount)
print("the converted rate is: ", output)