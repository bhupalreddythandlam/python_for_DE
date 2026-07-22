fruits = {
    "apple"  :  90,
    "banana" : 40,
    "mango"  : 100
}
discount_fruits={}
for k,v in fruits.items():
    discount_fruits[k]=v-5
print(discount_fruits)

# Dictionary comprehension version

#problem 1

'''
calculates the anual salary of the employee,
based on the monthly salaries
'''

monthly_salary = {"bob" : 90000,
                  "alex" : 100000,
                  "john"  : 120000}
anual_salary = {a:b*12 for a,b in monthly_salary.items()}
print(anual_salary)

#problem 2

'''
create a new dictionary of only the servers with an
uptime strictly less than 99.0
'''
server_uptimes = {"server-A": 99.9, "server-B": 98.5, "server-C": 100.0, "server-D": 95.0}
strict_server_uptime = {s:t for s,t in server_uptimes.items() if t<99.0}
print(strict_server_uptime)