
#problem 3

daily_revenue = {"Monday": "$1000", "Tuesday": "$1500", "Wednesday": "$800"}
'''
having the dictonary with daily revenues but the 
values are string with dollar sign,we want to conver the values in to int 
and remove the dollar sign fromthe value.
'''

daily_revenue_int = {day:int(revenue.replace("$"," ")) for day,revenue in daily_revenue.items()}
print(daily_revenue_int)

#problem 4

user_emails = {"user_1": "alice@email.com", "user_2": None, "user_3": "charlie@email.com", "user_4": None}
'''
create a new dictionary containing only the users who actually have an email address
'''

user_valid_emails = {user:mail for user,mail in user_emails.items() if mail is not None}
print("valid users :",user_valid_emails)
user_invalid_emails = {user:mail for user,mail in user_emails.items() if mail is None}
print("invalid users : ",user_invalid_emails)

