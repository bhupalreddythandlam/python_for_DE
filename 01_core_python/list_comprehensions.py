prices = [10,20,30]
doubled=[]
for i in prices:
    doubled.append(i*2)
print("doubledprices: ",doubled)

# List comprehension version

car_prices = [200000,300000,9000000]
discount_price=[i*0.9 for i in car_prices]
print("discount prices : ",discount_price)

#exercies on it
'''
list comprehension to convert celsius to Fahrenheit
'''
celsius_temps = [0, 10, 20, 30]
fahrenheit_temps = [(i*9/5)+32 for i in celsius_temps]
print("fahrenheit tempatures : ",fahrenheit_temps)

'''
String Cleaning

notes:
lower() converts the string in to lower cases
strip() removes the extra space at beginning and end of the string
'''
columns = [" id ", "Name ", " AGE"]
cleaned_columns = [string.strip().lower() for string in columns]
print("cleaned columns: ",cleaned_columns)

'''
Filtering Data

note:
it remove the negitive transactions from the list.
'''
transactions = [-50, 120, -20, 300]
correct_transactions=[amount for amount in transactions if amount > 0]
print("correct transactions: ",correct_transactions)