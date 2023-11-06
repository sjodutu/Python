print("There are rules to this when you provide a phrase or the full word remember to add a space where it is need e.g grand theft auto is written as grand theft auto not grandtheftauto")
users_input = input("Enter Phrase: ")

text = users_input.split()
z = text[0][0].upper() + text[1][0].upper() + text[2][0].upper()
print(z)

'''
a = " "
for i in text:
    a = a + i[0]
print(a)
'''