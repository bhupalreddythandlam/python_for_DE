try:
    for i in range(1,10):
        print(j)
except NameError:
    print("there is a name error check the code again!")

'''
this is the sample program for error handling
'''

total_sales = 5000
num_orders = 0
try:
    print(total_sales/num_orders)
except ZeroDivisionError:
    print("number of orders is zero!")

# problem 1

stock_levels = ["150", "200", "Out of Stock", "85"]

# convert each item to an int()

try:
    stock_levels_int = [int(level) for level in stock_levels]
    print(stock_levels_int)
except ValueError:
    print("bad values")

# problem 2

api_response = {"temperature": 75, "city": "Miami", "wind": "10mph",}

# key value error 
# Write a try / except block that tries to print api_response["humidity"]. If it hits a KeyError, catch it and print "Humidity data missing."

try:
    if api_response["humidity"]:
        print(api_response["humidity"])
except KeyError:
    print("humidity data missing!")

# problem 3
uptime_data = {"server_1": "45", "server_2": "error"}
servers_to_check = ["server_1", "server_2", "server_3"]

'''
goal is to loop through servers_to_check and 
try to print the server's uptime as an integer using int(uptime_data[server]
'''

for server in servers_to_check:
    try:
        print(f"{server} : {int(uptime_data[server]) }")
    except ValueError:
        print(f"value error at {server} : {uptime_data[server]}")
    except KeyError:
        print(f"key error at {server}")
    finally:
        print(f"--- Check complete for {server} ---")
