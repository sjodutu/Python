'''
email = input("Please Enter your email: ")
user_name = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
print(user_name)
print(domain_name)
'''

#  or we can do it this way
email = input("Please Enter your email: ")
result = email.split('@')
user_name = result[0]
domain_name = result[1]
# with split i can place the username and domain into arrays and remember that arrays have indexes
print(f'Your email is {email}, your username is {user_name} and your domain name is {domain_name}')
